---
title: "[feature] Add a --pdf option to the cost estimator"
labels: ["enhancement"]
---

The perc test logger has a `--pdf` option for exporting a branded report. Could we add the same to `outwestseptic_cost_estimator.py`?

**Why**

When I'm quoting on-site, I run the cost estimator interactively. The customer asks "what does that look like on paper?" and right now I have to manually type it into the quote builder Excel workbook. A `--pdf` flag would let me print or email a planning-estimate PDF right from the CLI.

**What I'd want**

- A `--pdf PATH` flag
- Branded PDF with the Out West Septic header and footer
- Same content as the text output (project, modifiers, range, midpoint, disclaimer)
- One page, landscape or portrait, whichever fits better

**Affected files**

- `scripts/outwestseptic_cost_estimator.py`

**Notes**

The reportlab dependency is already in `requirements.txt` for the perc logger. So no new deps.

I can write the function and submit a PR if you want to focus on other things.

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — OS0041298*