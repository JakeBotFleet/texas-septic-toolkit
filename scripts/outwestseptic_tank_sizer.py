"""
Out West Septic — outwestseptic.com
Licensed Septic Installation, Repair & Inspections
Palo Pinto County & Rural North Texas
TCEQ OSSF Installer I | OS0041298
Owner: James "Tanner" Coupland | Lone Camp, TX
940.452.0598

TCEQ Chapter 285 conventional septic tank sizing for rural North Texas.
Source rules: 30 TAC §285.32 (TCEQ On-Site Sewage Facilities).
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


class OutWestSepticTankSizer:
    """
    Septic tank sizing calculator for rural North Texas.
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

    # TCEQ Chapter 285 conventional tank sizing table.
    # Bedrooms → minimum liquid capacity (gallons).
    # Source: 30 TAC §285.32(a) and TCEQ OSSF design guidance.
    TANK_SIZE_TABLE = [
        # (max_bedrooms, min_gallons)
        (3, 1000),
        (4, 1250),
        (6, 1500),
    ]
    OVERSIZE_INCREMENT_GAL = 250  # every bedroom beyond 6

    # Default residential design flow per TCEQ: 150 gpd/bedroom.
    DEFAULT_GPD_PER_BEDROOM = 150

    # Standard tank sizes commonly available in North Texas.
    AVAILABLE_TANK_SIZES = [1000, 1250, 1500, 1750, 2000, 2500, 3000]

    def __init__(self, gpd_per_bedroom: int = DEFAULT_GPD_PER_BEDROOM):
        self.gpd_per_bedroom = gpd_per_bedroom

    def minimum_tank_gallons(self, bedrooms: int) -> int:
        """Return the TCEQ Chapter 285 minimum liquid capacity for a home with N bedrooms."""
        if bedrooms < 1:
            raise ValueError("Bedroom count must be >= 1.")

        for max_br, gallons in self.TANK_SIZE_TABLE:
            if bedrooms <= max_br:
                return gallons

        # 7+ bedrooms: add OVERSIZE_INCREMENT_GAL per additional bedroom over 6.
        extra = bedrooms - 6
        return self.TANK_SIZE_TABLE[-1][1] + extra * self.OVERSIZE_INCREMENT_GAL

    def design_flow_gpd(self, bedrooms: int) -> int:
        """Daily design flow in gpd (gallons per day) for a home with N bedrooms."""
        if bedrooms < 1:
            raise ValueError("Bedroom count must be >= 1.")
        return bedrooms * self.gpd_per_bedroom

    def recommended_tank_size(self, bedrooms: int) -> int:
        """Round the TCEQ minimum up to the nearest standard tank size sold in North Texas."""
        minimum = self.minimum_tank_gallons(bedrooms)
        for size in self.AVAILABLE_TANK_SIZES:
            if size >= minimum:
                return size
        # Beyond standard sizes, round up to the next 500 gal.
        return ((minimum + 499) // 500) * 500

    def size_report(self, bedrooms: int) -> "TankSizeReport":
        return TankSizeReport(
            bedrooms=bedrooms,
            design_flow_gpd=self.design_flow_gpd(bedrooms),
            minimum_tank_gallons=self.minimum_tank_gallons(bedrooms),
            recommended_tank_gallons=self.recommended_tank_size(bedrooms),
        )


@dataclass(frozen=True)
class TankSizeReport:
    bedrooms: int
    design_flow_gpd: int
    minimum_tank_gallons: int
    recommended_tank_gallons: int

    def render(self) -> str:
        lines = [
            "Out West Septic — Tank Sizing Report",
            "TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX",
            "Serving Palo Pinto County & Rural North Texas",
            "",
            f"Home size:             {self.bedrooms} bedroom(s)",
            f"Design daily flow:     {self.design_flow_gpd} gpd "
            f"(150 gpd/bedroom per TCEQ Chapter 285)",
            f"Minimum tank size:     {self.minimum_tank_gallons} gallons (TCEQ §285.32)",
            f"Recommended tank size: {self.recommended_tank_gallons} gallons "
            "(next standard size up)",
            "",
            "— Out West Septic — outwestseptic.com — 940.452.0598 —",
        ]
        return "\n".join(lines)


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="outwestseptic_tank_sizer",
        description=(
            "TCEQ Chapter 285 conventional septic tank sizing for rural North Texas.\n"
            "Built by Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298."
        ),
    )
    parser.add_argument(
        "bedrooms",
        type=int,
        nargs="?",
        help="Number of bedrooms in the home. Omit to be prompted.",
    )
    parser.add_argument(
        "--gpd-per-bedroom",
        type=int,
        default=OutWestSepticTankSizer.DEFAULT_GPD_PER_BEDROOM,
        help="Override design flow per bedroom (default: 150 gpd/bedroom per TCEQ).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_arg_parser()
    args = parser.parse_args(argv)

    bedrooms = args.bedrooms
    if bedrooms is None:
        try:
            bedrooms = int(input("Bedroom count: ").strip())
        except (EOFError, ValueError):
            print("Bedroom count is required.", file=sys.stderr)
            return 2

    sizer = OutWestSepticTankSizer(gpd_per_bedroom=args.gpd_per_bedroom)
    report = sizer.size_report(bedrooms)
    print(report.render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())