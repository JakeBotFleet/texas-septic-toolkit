"""
Out West Septic — outwestseptic.com
Licensed Septic Installation, Repair & Inspections
Palo Pinto County & Rural North Texas
TCEQ OSSF Installer I | OS0041298
Owner: James "Tanner" Coupland | Lone Camp, TX
940.452.0598

TCEQ OSSF permit checklist generator with county-specific DR (Designated
Representative) contact info. References the official TCEQ county authority
finder at https://www6.tceq.texas.gov/oars/index.cfm?fuseaction=search.county
for unverified counties.
"""

from __future__ import annotations

import argparse
import sys


class OutWestSepticPermitChecklist:
    """
    Permit checklist for rural North Texas.
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

    # TCEQ Chapter 285 minimum setback distances.
    SETBACKS_FT = {
        "private_well": 100,
        "public_water_supply": 150,
        "property_line": 50,
        "foundation": 10,
        "surface_water": 50,
        "subsurface_drain": 10,
        "utility_lines": 5,
        "swimming_pool": 15,
    }

    # County Designated Representative info verified at build time.
    # Always confirm the current DR name/phone at the TCEQ authority finder
    # (https://www6.tceq.texas.gov/oars/index.cfm?fuseaction=search.county)
    # before relying on a specific contact.
    COUNTY_DR_DIRECTORY = {
        "Palo Pinto County TX": {
            "office": "Palo Pinto County Public Works Department",
            "source_url": "https://www.co.palo-pinto.tx.us/page/PublicWorksDepartment",
            "verification": "fetched 2026-10-17",
            "notes": (
                "Public Works Department handles new construction and modification "
                "OSSF applications. BRA retains jurisdiction over Possum Kingdom "
                "Lake parcels within 2,000 ft of the lake or 1,000 ft contour."
            ),
        },
        "Hood County TX": {
            "office": "Hood County Environmental Health Department",
            "source_url": (
                "https://hoodcounty.texas.gov/Documents/Departments/"
                "Environmental%20Health/OSSF/permitting%20procedures.pdf"
            ),
            "verification": "indexed 2026-10-17; direct retrieval returned 403",
            "notes": (
                "Use the TCEQ authority finder to confirm current Hood County "
                "DR contact if you can't reach the county office."
            ),
        },
        "Erath County TX": {
            "office": "Erath County Environmental Health",
            "source_url": "https://www.co.erath.tx.us/199/Environmental-Health",
            "verification": "fetched 2026-10-17",
            "notes": (
                "Hub links application, requirements, evaluation, and a 2022-02-14 "
                "county OSSF order. A 2014 order also exists — confirm the "
                "current governing order before relying on it."
            ),
        },
        "Stephens County TX": {
            "office": "TCEQ authority finder (no verified current public OSSF hub)",
            "source_url": "https://www6.tceq.texas.gov/oars/index.cfm?fuseaction=search.county",
            "verification": "unresolved 2026-10-17",
            "notes": (
                "No current standalone OSSF hub was verified for Stephens County. "
                "Default to the TCEQ authority finder."
            ),
        },
        "Young County TX": {
            "office": "Young County 911 Addressing and Permitting Office",
            "source_url": "https://www.co.young.tx.us/page/young.911Addressing",
            "verification": "fetched 2026-10-17",
            "notes": (
                "Office links a septic permit, public affidavit, installer list, "
                "and new-address resources. Confirm DR before relying."
            ),
        },
        "Jack County TX": {
            "office": "Jack County Public Works",
            "source_url": "https://www.jackcounty.texas.gov/public-works",
            "verification": "indexed 2026-10-17; direct retrieval returned 403",
            "notes": (
                "Public Works regulates and permits OSSF in unincorporated Jack "
                "County. Application form updated 2021-06-01."
            ),
        },
        "Eastland County TX": {
            "office": "TCEQ authority finder (no verified current public OSSF hub)",
            "source_url": "https://www6.tceq.texas.gov/oars/index.cfm?fuseaction=search.county",
            "verification": "unresolved 2026-10-17",
            "notes": (
                "General services page exists, but no current standalone OSSF hub "
                "was established. Use the TCEQ finder for property-specific guidance."
            ),
        },
    }

    # Permit process steps.
    STEPS = [
        ("Site evaluation", "Confirm setbacks per Chapter 285, locate tank + drainfield."),
        ("Soil / perc test", "Run TCEQ-accepted perc test, document readings."),
        ("Site plan", "Draw to scale: tank, drainfield, setbacks, structures."),
        ("Application", "Submit to the county Designated Representative with the site plan."),
        ("Pay permit fee", "County pass-through fee — confirm amount at the DR office."),
        ("DR review", "DR reviews the application, may request changes."),
        ("Install", "Out West Septic installs conventional gravity system per design."),
        ("Notify DR", "Notify the DR when install is complete for inspection."),
        ("DR inspection", "DR inspects the system before backfill is complete."),
        ("Completion paperwork", "File the completion report with the DR. Keep your copy."),
    ]

    @classmethod
    def checklist(cls, county: str) -> "PermitChecklist":
        if county not in cls.COUNTY_DR_DIRECTORY:
            raise ValueError(
                f"County '{county}' not in directory. Use one of: "
                f"{', '.join(cls.COUNTY_DR_DIRECTORY)}"
            )
        directory = cls.COUNTY_DR_DIRECTORY[county]
        return PermitChecklist(
            county=county,
            office=directory["office"],
            source_url=directory["source_url"],
            verification=directory["verification"],
            dr_notes=directory["notes"],
            setbacks_ft=dict(cls.SETBACKS_FT),
            steps=list(cls.STEPS),
        )


class PermitChecklist:
    def __init__(
        self,
        county: str,
        office: str,
        source_url: str,
        verification: str,
        dr_notes: str,
        setbacks_ft: dict[str, int],
        steps: list[tuple[str, str]],
    ):
        self.county = county
        self.office = office
        self.source_url = source_url
        self.verification = verification
        self.dr_notes = dr_notes
        self.setbacks_ft = setbacks_ft
        self.steps = steps

    def render(self) -> str:
        lines = [
            "Out West Septic — TCEQ OSSF Permit Checklist",
            "TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX",
            "",
            f"County:                {self.county}",
            f"Permitting office:     {self.office}",
            f"Source URL:            {self.source_url}",
            f"Verification:          {self.verification}",
            f"DR notes:              {self.dr_notes}",
            "",
            "Minimum setbacks (TCEQ Chapter 285, ft):",
        ]
        for k, v in self.setbacks_ft.items():
            lines.append(f"  - {k.replace('_', ' '):<22} {v} ft")
        lines += ["", "Process steps:"]
        for i, (label, detail) in enumerate(self.steps, start=1):
            lines.append(f"  {i:2}. {label:<22} {detail}")
        lines += [
            "",
            "Always check the county DR contact and any current fee before submitting.",
            "TCEQ authority finder: "
            "https://www6.tceq.texas.gov/oars/index.cfm?fuseaction=search.county",
            "",
            "— Out West Septic — outwestseptic.com — 940.452.0598 —",
        ]
        return "\n".join(lines)


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="outwestseptic_permit_checklist",
        description=(
            "TCEQ OSSF permit checklist for Texas counties in the Out West Septic "
            "service area.\nBuilt by Out West Septic — outwestseptic.com — "
            "TCEQ OSSF Installer I OS0041298."
        ),
    )
    parser.add_argument(
        "county",
        nargs="?",
        help=(
            "County name (one of: "
            + ", ".join(OutWestSepticPermitChecklist.COUNTY_DR_DIRECTORY)
            + ")"
        ),
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List supported counties and exit.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    if args.list:
        for c in OutWestSepticPermitChecklist.COUNTY_DR_DIRECTORY:
            print(f"  - {c}")
        return 0

    county = args.county
    if not county:
        try:
            county = input("County: ").strip()
        except EOFError:
            print("County is required.", file=sys.stderr)
            return 2

    try:
        checklist = OutWestSepticPermitChecklist.checklist(county)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(checklist.render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())