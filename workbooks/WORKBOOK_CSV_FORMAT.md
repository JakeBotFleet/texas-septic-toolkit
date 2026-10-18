# Blank workbook CSV format

These CSVs are editable record starters for the Out West Septic project, not Excel workbooks, executable schemas or automated forms. They replace the older drafts that supplied prices, soil measurements, design formulas and inspection scores without evidence.

- [Observation report starter](outwestseptic_inspection_report.csv): 33 field rows.
- [Site-information starter](outwestseptic_site_assessment.csv): 42 field rows.
- [Observation worksheet](outwestseptic_inspection_report.md) and [site worksheet](outwestseptic_site_assessment.md) explain the manual workflow.

## Columns

| Column | Meaning |
|---|---|
| section | Worksheet section |
| record_id | Group identifier; replace template IDs when creating actual records |
| field | Stable field name within a group |
| type | Suggested input type: text, date, integer or number; no software enforcement |
| unit | Fixed unit where defined; generic measurement groups provide a separate measurement_unit field |
| value | User-supplied value; blank in the distributed starter |
| status | User-supplied evidence state; blank means unrecorded |
| evidence_reference | Evidence ID or authorized private reference supporting the value |
| recorded_by | Actual person or record source; no prefilled identity |
| recorded_on | Actual recording date/time and timezone where relevant |
| notes | Field instructions; never a measurement or approved business policy |

Duplicate all rows in a template group to add another observation, record, criterion or finding. Assign each group a unique record_id. The combination of section, record_id and field must remain unique.

For status, use observed, reported, not_accessed, not_tested, not_evaluated, not_observed_to_limit, not_applicable or unknown as appropriate. Explain limits and inapplicability in notes. Blank means unrecorded; it is not a satisfactory observation. A measured zero needs an explicit status and evidence. A missing measurement stays blank with its status, rather than putting "unknown" into a numeric value.

Dates should be recorded as text in a consistent format such as YYYY-MM-DD. Import identifier, date and text columns as text when using a spreadsheet. There are no formulas, macros, lookups, hidden defaults, scores or automated validation in these files.

The generic measurement_value fields require an accompanying measurement_unit in the same record group. Fixed-unit numeric fields do not establish a design input's applicability; the responsible professional supplies and reviews that evidence.

Keep completed customer records and evidence privately. This public distribution contains only field definitions and blank user-input columns.

## Distribution check

The accompanying `validate_blank_workbook_templates.py` checks the blank distribution structure, unique fields, type/unit metadata and absence of prefilled user values. It does not validate completed reports, regulatory compliance or professional conclusions.
