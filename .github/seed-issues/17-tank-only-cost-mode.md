---
title: "[feature] Cost estimator: add a tank-only replacement mode"
labels: ["enhancement"]
---

The cost estimator has a `tank_replacement` project type that covers replacing just the tank (existing drainfield OK). Could we add a similar mode for tank-only replacement where the drainfield is NOT OK?

The current `tank_replacement` assumes the existing drainfield works. On real jobs in Palo Pinto County, sometimes the tank is the obvious failure but the drainfield is borderline or already failing.

**What I'd want**

- A `tank_replacement_with_drainfield_concern` project type
- Or a flag like `--drainfield-condition marginal|fail|unknown` that adjusts the estimate
- The output makes the assumption explicit

**Why**

The current `tank_replacement` range is $2,500-$5,000. If I quote that and find out on day 2 that the drainfield is borderline, I'm going to come back to the customer with a $4k-$10k change order. Better to flag the risk upfront.

**Affected files**

- `scripts/outwestseptic_cost_estimator.py`

**Worked example**

```
python outwestseptic_cost_estimator.py tank_replacement --drainfield-condition marginal
# Output range adjusts upward to $3,500-$7,000 with a note about drainfield risk
```

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*