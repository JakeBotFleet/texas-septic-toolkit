"""Validate distributed blank CSV starters; not completed site/report records."""
from __future__ import annotations

import csv
from pathlib import Path
import sys

HEADER = [
    "section", "record_id", "field", "type", "unit", "value", "status",
    "evidence_reference", "recorded_by", "recorded_on", "notes",
]
USER_COLUMNS = ("value", "status", "evidence_reference", "recorded_by", "recorded_on")
TYPES = {"text", "date", "integer", "number"}


def validate_rows(rows: list[list[str]]) -> list[str]:
    """Check structure and unsafe defaults without interpreting professional facts."""
    if not rows or rows[0] != HEADER:
        return ["header must match the documented blank-template format"]
    if len(rows) == 1:
        return ["template contains no field rows"]
    errors: list[str] = []
    fields: set[tuple[str, str, str]] = set()
    numeric_without_unit: list[tuple[int, str, str, str]] = []
    for line, values in enumerate(rows[1:], 2):
        if len(values) != len(HEADER):
            errors.append(f"line {line}: expected {len(HEADER)} columns, got {len(values)}")
            continue
        row = dict(zip(HEADER, values))
        key = (row["section"], row["record_id"], row["field"])
        if not all(part.strip() for part in key):
            errors.append(f"line {line}: section, record_id and field must be present")
        if key in fields:
            errors.append(f"line {line}: duplicate field {key!r}")
        fields.add(key)
        if row["type"] not in TYPES:
            errors.append(f"line {line}: unsupported type {row['type']!r}")
        if any(row[column] != "" for column in USER_COLUMNS):
            errors.append(f"line {line}: distributed user-input columns must be blank")
        if not row["notes"].strip():
            errors.append(f"line {line}: field guidance is missing")
        if row["type"] in {"integer", "number"} and not row["unit"]:
            numeric_without_unit.append((line, *key))
    for line, section, record_id, field in numeric_without_unit:
        if field != "measurement_value" or (section, record_id, "measurement_unit") not in fields:
            errors.append(f"line {line}: numeric field needs a fixed unit or measurement_unit partner")
    return errors


def main(args: list[str]) -> int:
    if not args:
        print("Usage: python validate_blank_workbook_templates.py TEMPLATE.csv [...]", file=sys.stderr)
        return 2
    failed = False
    for filename in args:
        path = Path(filename)
        try:
            with path.open(encoding="utf-8-sig", newline="") as stream:
                rows = list(csv.reader(stream, strict=True))
            errors = validate_rows(rows)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors = [f"cannot read CSV: {exc}"]
        for error in errors:
            print(f"{path.name}: {error}", file=sys.stderr)
        if errors:
            failed = True
        else:
            print(f"{path.name}: valid blank template ({len(rows) - 1} fields)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
