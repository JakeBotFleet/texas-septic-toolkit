---
title: "[feature] Support exporting the inspection report to JSON"
labels: ["enhancement"]
---

For real estate transactions, the buyer's lender sometimes wants machine-readable data. A JSON export option for the inspection report would let me feed the inspection results into a lender's intake form without manual re-entry.

**What I'd want**

- A `--json PATH` flag on a new `outwestseptic_inspection_report.py` (the script doesn't exist yet — it could be a CLI wrapper around the workbook spec, or a standalone script that prompts for the same fields)
- JSON schema with: site address, county, date, inspector (Tanner Coupland, OS0041298), tank fields, drainfield fields, site fields, verdict, recommended next steps
- Pretty-printed, single file

**Why**

Right now I fill in the Excel workbook and export to PDF. The lender wants JSON. Adding JSON output to a script would save 30 minutes per inspection.

**Affected files**

- New file: `scripts/outwestseptic_inspection_report.py`
- Could share schema with `workbooks/outwestseptic_inspection_report.md` if that helps

**North Texas context**

Palo Pinto County is the most common. Hood and Erath next. JSON export should work for any of the seven priority counties.

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*