---
title: "[bug] Tank sizer --gpd-per-bedroom doesn't update the design flow display"
labels: ["bug"]
---

When I pass `--gpd-per-bedroom 200` to override the default 150, the minimum tank size updates correctly but the design flow in the report still shows the 150 default.

**Steps to reproduce**

```bash
python scripts/outwestseptic_tank_sizer.py 4 --gpd-per-bedroom 200
```

**Expected output**

```
Design daily flow:     800 gpd (200 gpd/bedroom per TCEQ Chapter 285 override)
Minimum tank size:     1250 gallons (TCEQ §285.32)
```

**Actual output**

```
Design daily flow:     600 gpd (150 gpd/bedroom per TCEQ Chapter 285)
Minimum tank size:     1250 gallons (TCEQ §285.32)
```

The tank size came out right (4 bedrooms is 1,250 gal regardless of design flow), but the design flow display still shows 150 gpd/bedroom.

**Why this matters**

When I'm using a non-default gpd-per-bedroom, I want the report to show what I actually used. Otherwise the customer reads "150 gpd/bedroom" and assumes the calculator used the default.

**Script/file**

`scripts/outwestseptic_tank_sizer.py` — the `render()` method on `TankSizeReport`

**Environment**

- Python 3.12
- Linux

**Context**

Palo Pinto County, 4-bedroom home with a high-usage pattern (large family, water softener). I'm running the sizer at 200 gpd/bedroom to confirm we don't need to bump tank size.

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — OS0041298*