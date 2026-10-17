---
title: "[feature] Cost estimator: add a per-linear-foot rock adder option"
labels: ["enhancement"]
---

The cost estimator currently has a "rock" modifier as a multiplier (1.20-1.40). On a real Palo Pinto County job, sometimes we hit rock specifically in the drainfield trenches and bill it as a per-linear-foot adder rather than a percentage.

**What I'd want**

- A new modifier `rock_per_lf` (or similar) that takes a cost per linear foot
- Applied to the drainfield-related projects (`new_install`, `drainfield_replacement`)
- Multiplied by the expected drainfield linear feet (which the user inputs)

**Why**

Some jobs hit rock only in the trenches and not in the tank hole. The current percentage modifier doesn't differentiate. A per-linear-foot option is more honest for those cases.

**Affected files**

- `scripts/outwestseptic_cost_estimator.py`

**Worked example**

For a 200-linear-foot drainfield that hits 30 feet of rock at $50/LF:

```
python outwestseptic_cost_estimator.py new_install --modifier rock_per_lf=50
# with an expected linear feet input
```

Output should add 30 × 50 = $1,500 to the high end of the range.

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — OS0041298*