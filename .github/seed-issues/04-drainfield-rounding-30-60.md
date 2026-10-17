---
title: "[bug] Drainfield calc rounding looks off for 30-60 min/in bracket"
labels: ["bug"]
---

Working through the math on a Thurber-clay lot (45 min/in) for a 4-bedroom home (500 gpd). The drainfield calc gives me an absorption area that doesn't seem right.

**Script/file**

`outwestseptic_drainfield_calc.py`

**Input**

```
perc=45
gpd=500
```

**Output**

```
Required absorption: 1650 sq ft
```

**Expected**

Per TCEQ §285.32, the 30-60 min/in bracket is **330 sq ft per 100 gpd**. So for 500 gpd that's 500 × 330 / 100 = **1,650 sq ft**. OK that's actually what I got.

But the script also rounds up to whole sq ft in a way that I want to double-check. The `int(-(-x // 100))` pattern is fine for 330 sq ft per 100 gpd, but the division comes before the rounding. Let me trace through...

Actually I think the output is correct. Disregard unless someone else sees a discrepancy. Filing this as a "verify" item rather than a confirmed bug.

If this is a non-bug, please close and add a comment confirming the math.

**Environment**

- Python 3.12
- macOS 14

**Context**

Thurber clay, Palo Pinto County. Looking at the math because I'm quoting a 4-bedroom build on a Thurber lot.

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — OS0041298*