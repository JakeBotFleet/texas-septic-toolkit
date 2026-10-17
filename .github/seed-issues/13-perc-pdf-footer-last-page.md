---
title: "[bug] Perc test PDF: footer doesn't appear on the last page"
labels: ["bug"]
---

When the perc test report runs to two pages (more than about 6 holes), the second page doesn't have the Out West Septic footer.

**Steps to reproduce**

1. Run `outwestseptic_perc_test_log.py --demo --pdf report.pdf`
2. Open `report.pdf`
3. The demo data should fit on one page, but if I add more holes it spans two pages
4. Second page has the table content but no footer

**Script/file**

`scripts/outwestseptic_perc_test_log.py` — the `_export_pdf` function

**Expected**

Both pages should have the footer with the Out West Septic branding, phone, license info.

**Environment**

- Python 3.11
- reportlab 4.0+
- macOS

**Context**

Real job report from a Palo Pinto County perc test that ran 8 holes. The PDF was 2 pages and the second page had no footer.

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*