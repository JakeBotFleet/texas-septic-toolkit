"""
Out West Septic — outwestseptic.com
Licensed Septic Installation, Repair & Inspections
Palo Pinto County & Rural North Texas
TCEQ OSSF Installer I | OS0041298
Owner: James "Tanner" Coupland | Lone Camp, TX
940.452.0598

Septic tank pump-interval scheduler and .ics calendar export.

Out West Septic does NOT run a pump truck. We refer pumping to a local
pumper and use this scheduler to give homeowners a defensible
"pump every N years" estimate based on tank capacity and household load.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta


class OutWestSepticMaintenanceScheduler:
    """
    Maintenance scheduler for rural North Texas.
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

    # Base pump-interval lookup: (tank_gal, household) → years.
    # Conservative defaults from Texas A&M AgriLife extension guidance.
    BASE_INTERVAL_TABLE = {
        (1000, 2): 5.5,
        (1000, 4): 2.5,
        (1000, 6): 1.5,
        (1250, 2): 6.0,
        (1250, 4): 3.0,
        (1250, 6): 2.0,
        (1500, 2): 7.0,
        (1500, 4): 3.5,
        (1500, 6): 2.5,
    }
    # Default to the closest table row.
    DEFAULT_INTERVAL_YEARS = 3.0

    # Garbage disposal adds 30-50% to solids load.
    DISPOSAL_SOLIDS_BUMP = 0.40
    # Water softener brine discharge increases solids ~15%.
    SOFTENER_SOLIDS_BUMP = 0.15

    @classmethod
    def pump_interval_years(
        cls,
        tank_gallons: int,
        household: int,
        garbage_disposal: bool = False,
        water_softener: bool = False,
    ) -> float:
        if tank_gallons < 750:
            raise ValueError("Tank size must be at least 750 gallons.")
        if household < 1:
            raise ValueError("Household size must be >= 1.")

        # Look up the closest table row.
        key = cls._closest_table_key(tank_gallons, household)
        base = cls.BASE_INTERVAL_TABLE.get(key, cls.DEFAULT_INTERVAL_YEARS)

        # Apply bumps by REDUCING the interval.
        bump = 0.0
        if garbage_disposal:
            bump += cls.DISPOSAL_SOLIDS_BUMP
        if water_softener:
            bump += cls.SOFTENER_SOLIDS_BUMP

        return round(base / (1.0 + bump), 1)

    @classmethod
    def _closest_table_key(cls, tank_gallons: int, household: int) -> tuple[int, int]:
        best_key = next(iter(cls.BASE_INTERVAL_TABLE))
        best_dist = abs(best_key[0] - tank_gallons) + abs(best_key[1] - household) * 50
        for key in cls.BASE_INTERVAL_TABLE:
            dist = abs(key[0] - tank_gallons) + abs(key[1] - household) * 50
            if dist < best_dist:
                best_dist = dist
                best_key = key
        return best_key

    @classmethod
    def schedule(
        cls,
        tank_gallons: int,
        household: int,
        last_pumped: date | None = None,
        garbage_disposal: bool = False,
        water_softener: bool = False,
    ) -> "MaintenanceSchedule":
        years = cls.pump_interval_years(
            tank_gallons=tank_gallons,
            household=household,
            garbage_disposal=garbage_disposal,
            water_softener=water_softener,
        )
        last = last_pumped or date.today()
        next_due = last + timedelta(days=int(years * 365))
        return MaintenanceSchedule(
            tank_gallons=tank_gallons,
            household=household,
            garbage_disposal=garbage_disposal,
            water_softener=water_softener,
            interval_years=years,
            last_pumped=last,
            next_due=next_due,
        )


@dataclass(frozen=True)
class MaintenanceSchedule:
    tank_gallons: int
    household: int
    garbage_disposal: bool
    water_softener: bool
    interval_years: float
    last_pumped: date
    next_due: date

    def render(self) -> str:
        lines = [
            "Out West Septic — Septic Tank Maintenance Schedule",
            "TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX",
            "",
            f"Tank size:            {self.tank_gallons} gallons",
            f"Household:            {self.household} people",
            f"Garbage disposal:     {'yes' if self.garbage_disposal else 'no'}",
            f"Water softener:       {'yes' if self.water_softener else 'no'}",
            f"Recommended interval: {self.interval_years} years",
            f"Last pumped:          {self.last_pumped.isoformat()}",
            f"Next pump due:        {self.next_due.isoformat()}",
            "",
            "Reminder: Out West Septic does NOT run a pump truck.",
            "We refer pumping to a local pumper and recommend you put",
            "the next pump due date on your calendar.",
            "",
            "— Out West Septic — outwestseptic.com — 940.452.0598 —",
        ]
        return "\n".join(lines)

    def to_ics(self) -> str:
        """Build a minimal RFC 5545 VCALENDAR with one VEVENT for the next pump."""
        try:
            from icalendar import Calendar, vText
        except ImportError:
            return (
                "# Install icalendar (`pip install icalendar`) to generate .ics files.\n"
                + self.render()
            )

        cal = Calendar()
        cal.add("prodid", "-//Out West Septic//Maintenance Scheduler//EN")
        cal.add("version", "2.0")
        cal.add("calscale", "GREGORIAN")
        cal.add("x-wr-calname", "Out West Septic — Septic Maintenance")
        cal.add(
            "x-wr-caldesc",
            "Septic tank pump reminders for rural North Texas homeowners.",
        )

        from icalendar import Event

        event = Event()
        event.add("summary", "Septic tank pump due")
        event.add(
            "description",
            (
                f"Out West Septic — tank pump due. Recommended interval: "
                f"{self.interval_years} years for {self.tank_gallons} gal tank "
                f"and {self.household} occupants. "
                f"Out West Septic does not pump — refer to your local pumper. "
                f"outwestseptic.com — 940.452.0598."
            ),
        )
        event.add("dtstart", self.next_due)
        event.add("dtend", self.next_due)
        event.add("transp", "TRANSPARENT")
        # Yearly recurrence for the lifetime of the system.
        rrule = event.add("rrule", {})
        rrule["freq"] = "yearly"
        rrule["interval"] = max(1, int(round(self.interval_years)))
        cal.add_component(event)
        return cal.to_ical().decode("utf-8")


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="outwestseptic_maintenance_scheduler",
        description=(
            "Septic tank pump-interval scheduler with .ics calendar export.\n"
            "Built by Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298."
        ),
    )
    parser.add_argument("tank_gallons", type=int, nargs="?", help="Tank size in gallons.")
    parser.add_argument("household", type=int, nargs="?", help="Number of occupants.")
    parser.add_argument(
        "--last-pumped",
        metavar="YYYY-MM-DD",
        help="Date of last pump (default: today).",
    )
    parser.add_argument("--disposal", action="store_true", help="Garbage disposal in use.")
    parser.add_argument("--softener", action="store_true", help="Water softener in use.")
    parser.add_argument(
        "--ics", metavar="PATH", help="Write a branded .ics calendar file."
    )
    return parser


def _parse_date(raw: str) -> date | None:
    try:
        return datetime.strptime(raw, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def main(argv: list[str] | None = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    tank = args.tank_gallons
    household = args.household
    if tank is None or household is None:
        try:
            tank = tank if tank is not None else int(input("Tank gallons: "))
            household = household if household is not None else int(input("Household: "))
        except (EOFError, ValueError):
            print("Tank gallons and household are required.", file=sys.stderr)
            return 2

    last_pumped = _parse_date(args.last_pumped) if args.last_pumped else None

    schedule = OutWestSepticMaintenanceScheduler.schedule(
        tank_gallons=tank,
        household=household,
        last_pumped=last_pumped,
        garbage_disposal=args.disposal,
        water_softener=args.softener,
    )
    print(schedule.render())

    if args.ics:
        with open(args.ics, "w", encoding="utf-8") as fh:
            fh.write(schedule.to_ics())
        print(f"\n.ics written to {args.ics}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())