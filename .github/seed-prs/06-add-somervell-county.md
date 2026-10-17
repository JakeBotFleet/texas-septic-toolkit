---
title: "feat(permit-checklist): add Somervell County"
labels: ["enhancement"]
---

Closes #14

**What**

Adds a `Somervell County TX` entry to `outwestseptic_permit_checklist.py`'s `COUNTY_DR_DIRECTORY`.

**Why**

Glen Rose is in Somervell County. Real estate inspection scheduled there next month.

**Changes**

- New directory entry for Somervell County with verified DR routing
- Updated wiki navigation on Home.md

**Verified**

```bash
python scripts/outwestseptic_permit_checklist.py "Somervell County TX"
```

Output renders correctly.

---

*Out West Septic — TCEQ OSSF Installer I — OS0041298*