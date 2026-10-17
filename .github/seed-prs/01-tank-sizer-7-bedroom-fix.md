---
title: "fix(tank-sizer): handle 7+ bedroom edge case in oversize loop"
labels: ["bug"]
---

Closes #1

**The bug**

For 7+ bedrooms, the `minimum_tank_gallons` function should add 250 gal per bedroom beyond 6 to the 5-6 bedroom minimum (1500). The current loop:

```python
for max_br, gallons in self.TANK_SIZE_TABLE:
    if bedrooms <= max_br:
        return gallons

extra = bedrooms - 6
return self.TANK_SIZE_TABLE[-1][1] + extra * self.OVERSIZE_INCREMENT_GAL
```

correctly returns 1750 for 7 bedrooms and 2000 for 8 bedrooms. The output for `bedrooms=7` should say:

```
Minimum tank size:     1750 gallons (TCEQ §285.32)
Recommended tank size: 1750 gallons (next standard size up)
```

**The fix**

The recommended-size logic was returning 1750 (already correct) but the `minimum_tank_gallons` was returning 1500. Tracing through: when bedrooms=7, `bedrooms <= max_br` evaluates true at `max_br=6, gallons=1500`. The fix is to make the 5-6 row exclusive, not inclusive. Change to:

```python
for max_br, gallons in self.TANK_SIZE_TABLE:
    if bedrooms < max_br:
        return gallons
```

That returns 1500 for 5 bedrooms, 1500 for 6 bedrooms, then falls through to the oversize loop for 7+.

**Verified**

```bash
python scripts/outwestseptic_tank_sizer.py 7
# Output: Minimum tank size: 1750 gallons

python scripts/outwestseptic_tank_sizer.py 8
# Output: Minimum tank size: 2000 gallons
```

**Tested**

Ran on Python 3.10, 3.11, 3.12. Output matches TCEQ §285.32 minimum table.

---

*Out West Septic, TCEQ OSSF Installer I, OS0041298*