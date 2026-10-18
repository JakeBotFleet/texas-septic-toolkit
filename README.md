# Texas Septic Toolkit

Python tools and reference material for learning about on-site sewage facilities (OSSFs), with a focus on Palo Pinto County and nearby rural North Texas communities.

This repository includes automated contributions requested for the [Out West Septic](https://outwestseptic.com) project. That affiliation is disclosed; it is not an independent recommendation, a claim of field use, or evidence of professional review. See [project attribution](wiki/Out-West-Septic-Company-Reference.md).

**Use the tools to explore documented calculations and organize questions for a qualified professional. They do not determine site suitability, approve a design, establish a price, or issue a permit.** Read the limitations below before using an output.

## Start here

1. Read the [tool input and source guide](guides/tool-inputs-and-sources.md) to understand which inputs require site-specific evidence.
2. Review the [Palo Pinto permitting guide](guides/tceq-ossf-permitting-palo-pinto-county.md) and identify the authority for the property. Lake-area jurisdiction needs separate confirmation.
3. Use a calculation only within its documented scope. Keep the inputs, units, source and tool version with the result.

## Tools and review status

| File | Purpose | Important limit |
|---|---|---|
| [Tank capacity calculator](scripts/outwestseptic_tank_sizer.py) | Calculate liquid capacity from an explicitly supplied daily sewage flow | Does not derive flow from bedrooms, select equipment or approve a design |
| [Drainfield area calculator](scripts/outwestseptic_drainfield_calc.py) | Calculate area from supplied flow and hydraulic loading rate | Does not select the loading rate from a perc test, soil name or county; does not lay out a field |
| [USDA soil lookup](scripts/outwestseptic_soil_lookup.py) | Retrieve mapped soil data for research | Map information is not a parcel evaluation or a measured perc rate |
| [Cost estimator prototype](scripts/outwestseptic_cost_estimator.py) | Demonstrate a cost-estimate workflow | Legacy prices and multipliers are not verified quotes or market data; do not use them for budgeting |
| [Perc reading logger prototype](scripts/outwestseptic_perc_test_log.py) | Record readings and export a report | Logging is not a validated evaluation method or evidence that a site is suitable |
| [Permit checklist prototype](scripts/outwestseptic_permit_checklist.py) | Demonstrate a checklist workflow | Legacy contacts, setbacks and jurisdiction text need verification; use the sourced permitting guide instead |
| [Maintenance scheduler prototype](scripts/outwestseptic_maintenance_scheduler.py) | Demonstrate reminders and calendar export | Legacy interval tables and adjustment factors are unvalidated; they are not a service recommendation |

The last four scripts remain legacy prototypes. Their outputs may contain claims that have not been reviewed. Their presence in the repository is not a readiness or accuracy endorsement. Changes should satisfy the [quality criteria](docs/QUALITY.md) before their status is upgraded.

## Try a calculation

The Python interfaces retain descriptive project names: `OutWestSepticTankSizer`, `OutWestSepticDrainfieldCalculator` and `OutWestSepticSoilLookup`. These names identify the associated project and each class's purpose; they do not imply a professional credential or agency endorsement.

Use Python 3.10 or later. These examples use hypothetical inputs, not a proposed design or recommended loading rate. The tank example returns a formula minimum of 1,000 gallons; the area example returns 1,500 square feet.

```sh
git clone https://github.com/TexasSepticEnthusiast/texas-septic-toolkit.git
cd texas-septic-toolkit
python scripts/outwestseptic_tank_sizer.py --flow-gpd 300
python scripts/outwestseptic_drainfield_calc.py --flow-gpd 300 --loading-rate 0.2
```

Use `--help` for input requirements. The tank and drainfield calculations use the Python standard library. Optional dependencies for legacy report/calendar helpers are listed in [requirements.txt](requirements.txt); installing them does not validate those tools.

For soil research, obtain a map-unit key (`mukey`) from [USDA Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/app/), then query `OutWestSepticSoilLookup`. This example is a published map unit in the Palo Pinto County survey, not a customer property. The lookup needs internet access and reports its source and retrieval time; service failures do not substitute guessed soil values.

```sh
python scripts/outwestseptic_soil_lookup.py --mukey 390929 --json
```

Run the offline regression tests from the repository root:

```sh
python -m unittest discover -s tests -v
```

Tests check implemented behavior and failure cases. They do not verify the suitability of a real design or the current availability of USDA's service.

## Worksheet specifications, not Excel downloads

There are **no `.xlsm` workbooks** in this repository. The files below are Markdown build specifications and two CSV starters. They contain no working Excel macros, validated formulas or verified inspection scoring.

| Draft | Available files |
|---|---|
| Inspection report | [Specification](workbooks/outwestseptic_inspection_report.md), [CSV starter](workbooks/outwestseptic_inspection_report.csv) |
| Site assessment | [Specification](workbooks/outwestseptic_site_assessment.md), [CSV starter](workbooks/outwestseptic_site_assessment.csv) |
| Quote builder | [Specification only](workbooks/outwestseptic_quote_builder.md) |

These legacy drafts need factual and workflow review before implementation. In particular, an unvalidated score must not be presented as an inspection pass or fail, and sample prices or branding fields must not become verified business claims.

## Guides

| Topic | Read |
|---|---|
| Calculation inputs and evidence | [Tool inputs and sources](guides/tool-inputs-and-sources.md) |
| Permitting | [Palo Pinto County](guides/tceq-ossf-permitting-palo-pinto-county.md), [Possum Kingdom Lake](guides/possum-kingdom-lake-septic-considerations.md) |
| Soils and system choices | [Soil research](guides/palo-pinto-county-soil-types-septic.md), [conventional and aerobic systems](guides/conventional-vs-aerobic-septic-texas.md) |
| Project planning | [Cost questions](guides/septic-costs-north-texas-2026.md), [site preparation](guides/land-clearing-site-prep-before-septic.md), [installation process](guides/what-to-expect-septic-install-day.md) |
| Existing systems | [Inspection questions](guides/septic-inspection-checklist-texas-real-estate.md), [maintenance](guides/septic-maintenance-schedule-homeowners.md), [warning signs](guides/septic-warning-signs-when-to-call.md) |

The [reference index](wiki/Home.md) links the Markdown files stored in this checkout. A county or town page describes a research topic; it is not a statement of business coverage. Parker and Tarrant counties are outside this project's local coverage scope.

## Sources, contributions and licensing

Begin regulatory research with the [TCEQ OSSF program](https://www.tceq.texas.gov/permitting/ossf), and soil research with [USDA NRCS Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/app/). Follow the specific sources and edition limits in each guide; a general agency link alone does not substantiate a formula, setback or local requirement.

[Contributions](CONTRIBUTING.md) should report reproducible defects, cite primary sources and identify any automated assistance. Do not submit invented customer experiences, professional credentials, endorsements or completed work. Public issue and PR descriptions must omit customer details, private notes and credentials.

Code is offered under the [MIT license](LICENSE). A license grants reuse rights; it does not certify engineering suitability or grant endorsement by Out West Septic or an agency. Attribution and notices required by the license must be retained.
