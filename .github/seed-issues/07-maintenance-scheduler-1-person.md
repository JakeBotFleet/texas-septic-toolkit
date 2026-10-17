---
title: "[bug] Maintenance scheduler doesn't handle 1-person households well"
labels: ["bug"]
---

For a 1-person household with a 1000-gal tank, the recommended pump interval comes back as 5.5 years. That feels short — a single occupant generates far fewer solids than a 2-person household.

**Script/file**

`outwestseptic_maintenance_scheduler.py`

**Input**

```
tank=1000
household=1
```

**Output**

```
Recommended interval: 5.5 years
```

**What I'd expect**

A 1-person household should have a longer interval than 2-person. Maybe 7-8 years for a 1000-gal tank with a single occupant. The 2-person 1000-gal at 5.5 years is correct, but the script doesn't differentiate.

**Why it matters**

The pump-interval table in the script is keyed by (tank_gal, household) tuples. There's no row for household=1. The `_closest_table_key` function probably rounds to the 2-person row, which is fine, but it's worth documenting that 1-person is an under-approximation.

**Suggestion**

Either add explicit 1-person rows to the table or document the existing behavior more clearly in the script docstring.

**Environment**

- Python 3.10
- TCEQ AgriLife Extension guidance as the source

**Context**

Palo Pinto County, single-occupant home. Customer is on a well.

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — OS0041298*