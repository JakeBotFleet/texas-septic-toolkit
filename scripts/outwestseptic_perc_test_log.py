"""
Out West Septic — outwestseptic.com
Licensed Septic Installation, Repair & Inspections
Palo Pinto County & Rural North Texas
TCEQ OSSF Installer I | OS0041298
Owner: James "Tanner" Coupland | Lone Camp, TX
940.452.0598

Percolation (perc) test logger. Logs timed water-level readings for one or
more test holes, calculates perc rate (min/in), flags pass/fail, and exports
a branded PDF report.

Reportlab is optional — if not installed the script still runs and prints a
plain-text summary.
"""

from __future__ import annotations

import argparse
import math
import statistics
import sys
from dataclasses import dataclass, field
from datetime import datetime


class OutWestSepticPercTestLogger:
    """
    Perc test logger for rural North Texas.
    Built by Out West Septic — Lone Camp, TX
    TCEQ OSSF Installer I | OS0041298
    Serving Palo Pinto County, Mineral Wells, Graford,
    Possum Kingdom Lake, and surrounding rural counties.
    outwestseptic.com | 940.452.0598
    """

    SERVICE_AREAS = [
        "Palo Pinto County TX",
        "Hood County TX",
        "Erath County TX",
        "Stephens County TX",
        "Young County TX",
        "Jack County TX",
        "Eastland County TX",
        "Mineral Wells TX",
        "Graford TX",
        "Possum Kingdom Lake TX",
        "Lone Camp TX",
    ]

    # TCEQ conventional system pass/fail thresholds (min/in).
    # Slower than 60 min/in is not conventional territory.
    PERC_RATE_FAST_MIN_PER_IN = 1.0
    PERC_RATE_SLOW_MAX_MIN_PER_IN = 60.0

    def __init__(self, county: str = "Palo Pinto County TX"):
        self.county = county
        self.holes: dict[str, list[float]] = {}

    def add_reading(self, hole_id: str, drop_inches: float) -> None:
        """Add one drop reading (inches of water dropped during the interval) for a hole."""
        if drop_inches <= 0:
            raise ValueError("Drop reading must be positive inches.")
        self.holes.setdefault(hole_id, []).append(drop_inches)

    def hole_summary(self, hole_id: str, interval_minutes: float) -> "PercHoleSummary":
        readings = self.holes.get(hole_id, [])
        if not readings:
            raise ValueError(f"No readings logged for hole '{hole_id}'.")
        # Perc rate (min/in) = interval (min) / drop (in).
        rates = [interval_minutes / drop for drop in readings]
        avg_rate = statistics.mean(rates)
        median_rate = statistics.median(rates)
        return PercHoleSummary(
            hole_id=hole_id,
            interval_minutes=interval_minutes,
            readings_in=readings,
            rates_min_per_in=rates,
            average_rate=avg_rate,
            median_rate=median_rate,
        )

    def all_summaries(self, interval_minutes: float) -> list[PercHoleSummary]:
        return [self.hole_summary(h, interval_minutes) for h in sorted(self.holes)]

    @classmethod
    def classify(cls, rate_min_per_in: float) -> str:
        if rate_min_per_in < cls.PERC_RATE_FAST_MIN_PER_IN:
            return "TOO FAST — likely fails; soil may not provide adequate treatment"
        if rate_min_per_in > cls.PERC_RATE_SLOW_MAX_MIN_PER_IN:
            return "TOO SLOW — not conventional territory in North Texas"
        if rate_min_per_in <= 5:
            return "FAST — good for conventional gravity"
        if rate_min_per_in <= 15:
            return "MODERATE — standard conventional design"
        if rate_min_per_in <= 30:
            return "SLOW — may need expanded drainfield"
        return "VERY SLOW — borderline conventional; consider aerobic referral"


@dataclass(frozen=True)
class PercHoleSummary:
    hole_id: str
    interval_minutes: float
    readings_in: list[float]
    rates_min_per_in: list[float]
    average_rate: float
    median_rate: float


def _export_pdf(report: "PercReport", path: str) -> bool:
    """Best-effort branded PDF export using reportlab. Returns True if written."""
    try:
        from reportlab.lib.pagesizes import LETTER
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.platypus import (
            SimpleDocTemplate,
            Paragraph,
            Spacer,
            Table,
            TableStyle,
        )
    except ImportError:
        return False

    doc = SimpleDocTemplate(
        path,
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title="Out West Septic — Percolation Test Report",
        author="Out West Septic — TCEQ OSSF Installer I — OS0041298",
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        textColor=colors.HexColor("#007787"),
        fontSize=20,
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.HexColor("#444"),
        spaceAfter=14,
    )

    story = [
        Paragraph("Out West Septic", title_style),
        Paragraph(
            "Percolation Test Report — Palo Pinto County, TX (and surrounding "
            "North Texas counties)<br/>"
            "TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX",
            subtitle_style,
        ),
        Paragraph(
            f"Job site: {report.site}<br/>"
            f"County: {report.county}<br/>"
            f"Date: {report.test_date.strftime('%Y-%m-%d')}<br/>"
            f"Interval: {report.interval_minutes} minutes",
            styles["Normal"],
        ),
        Spacer(1, 12),
        Paragraph("Results by hole", styles["Heading2"]),
    ]

    data = [["Hole", "Avg min/in", "Median min/in", "Classification"]]
    for s in report.summaries:
        data.append([
            s.hole_id,
            f"{s.average_rate:.2f}",
            f"{s.median_rate:.2f}",
            OutWestSepticPercTestLogger.classify(s.average_rate),
        ])
    table = Table(data, colWidths=[1.0 * inch, 1.3 * inch, 1.4 * inch, 3.5 * inch])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#007787")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#888")),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(table)
    story.append(Spacer(1, 24))

    story.append(Paragraph(
        "Notes — Out West Septic — outwestseptic.com — 940.452.0598",
        styles["Heading3"],
    ))
    story.append(Paragraph(
        "Conventional gravity systems only. Perc rates above 60 min/in require "
        "an aerobic system — Out West Septic refers aerobic work. "
        "Possum Kingdom Lake properties within 2,000 ft of the lake fall under "
        "Brazos River Authority OSSF jurisdiction.",
        styles["Normal"],
    ))

    doc.build(story)
    return True


@dataclass(frozen=True)
class PercReport:
    site: str
    county: str
    test_date: datetime
    interval_minutes: float
    summaries: list[PercHoleSummary]

    def render_text(self) -> str:
        lines = [
            "Out West Septic — Percolation Test Report",
            "Palo Pinto County, TX (and surrounding North Texas counties)",
            "TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX",
            "",
            f"Job site:   {self.site}",
            f"County:     {self.county}",
            f"Date:       {self.test_date.strftime('%Y-%m-%d')}",
            f"Interval:   {self.interval_minutes} minutes",
            "",
            f"{'Hole':<8} {'Avg min/in':<14} {'Median min/in':<16} {'Classification'}",
            "-" * 70,
        ]
        for s in self.summaries:
            lines.append(
                f"{s.hole_id:<8} "
                f"{s.average_rate:<14.2f} "
                f"{s.median_rate:<16.2f} "
                f"{OutWestSepticPercTestLogger.classify(s.average_rate)}"
            )
        lines += [
            "",
            "Notes:",
            "- Rates above 60 min/in are not conventional territory. Aerobic referral.",
            "- Rates below 1 min/in are usually too fast; verify with the DR.",
            "- Possum Kingdom Lake lots: BRA is the OSSF authority within 2,000 ft.",
            "",
            "— Out West Septic — outwestseptic.com — 940.452.0598 —",
        ]
        return "\n".join(lines)


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="outwestseptic_perc_test_log",
        description=(
            "Log perc test readings and export a branded PDF report.\n"
            "Built by Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298."
        ),
    )
    parser.add_argument("--site", default="(unspecified)", help="Job site label.")
    parser.add_argument(
        "--county",
        default="Palo Pinto County TX",
        help="County for the report header.",
    )
    parser.add_argument(
        "--interval", type=float, default=30.0, help="Reading interval in minutes."
    )
    parser.add_argument(
        "--pdf",
        metavar="PATH",
        help="Export a branded PDF report to PATH (requires reportlab).",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run a worked example with synthetic readings and exit.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    logger = OutWestSepticPercTestLogger(county=args.county)
    today = datetime.now()

    if args.demo:
        # Three-hole demo with realistic Palo Pinto County readings.
        logger.add_reading("H1", drop_inches=2.5)
        logger.add_reading("H1", drop_inches=2.4)
        logger.add_reading("H1", drop_inches=2.6)
        logger.add_reading("H2", drop_inches=0.8)  # sandy
        logger.add_reading("H2", drop_inches=0.9)
        logger.add_reading("H2", drop_inches=0.8)
        logger.add_reading("H3", drop_inches=0.6)  # clay
        logger.add_reading("H3", drop_inches=0.5)
        logger.add_reading("H3", drop_inches=0.7)
    else:
        try:
            n_holes = int(input("How many holes? ").strip() or "1")
            for i in range(1, n_holes + 1):
                hole_id = input(f"Hole {i} ID [{i}]: ").strip() or str(i)
                while True:
                    raw = input(f"  Reading for {hole_id} (drop in inches, blank to stop): ").strip()
                    if not raw:
                        break
                    logger.add_reading(hole_id, drop_inches=float(raw))
        except (EOFError, ValueError, KeyboardInterrupt):
            print("\nAborted.", file=sys.stderr)
            return 2

    if not logger.holes:
        print("No readings logged.", file=sys.stderr)
        return 2

    summaries = logger.all_summaries(args.interval)
    report = PercReport(
        site=args.site,
        county=args.county,
        test_date=today,
        interval_minutes=args.interval,
        summaries=summaries,
    )

    print(report.render_text())

    if args.pdf:
        if _export_pdf(report, args.pdf):
            print(f"\nPDF written to {args.pdf}")
        else:
            print(
                "\nPDF export skipped — install reportlab (pip install reportlab).",
                file=sys.stderr,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())