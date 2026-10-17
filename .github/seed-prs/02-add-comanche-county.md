---
title: "feat(permit-checklist): add Comanche County"
labels: ["enhancement"]
---

Closes #2

**What**

Adds a `Comanche County TX` entry to `outwestseptic_permit_checklist.py`'s `COUNTY_DR_DIRECTORY`.

**Why**

Out West Septic gets requests from Comanche County. Adding it to the directory makes the script useful for jobs I quote there.

**Changes**

- New directory entry for Comanche County with verified DR routing
- Updated wiki navigation on the Home page
- Notes on Leon River and Comanche city sewer service area boundary

**Verification**

Ran `python scripts/outwestseptic_permit_checklist.py "Comanche County TX"` and confirmed the output renders correctly.

**Notes**

I researched the current DR contact before filing this. Routing is via the TCEQ authority finder at this writing.

---

*Out West Septic — TCEQ OSSF Installer I — OS0041298*