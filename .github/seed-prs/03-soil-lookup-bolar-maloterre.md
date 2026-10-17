---
title: "feat(soil-lookup): add Wise County soil presets (Bolar, Maloterre)"
labels: ["enhancement"]
---

Closes #3

**What**

Adds two new soil series to `outwestseptic_soil_lookup.py`'s `SOIL_PRESETS` table:

- **Bolar.** Clay loam, moderately well drained, typical perc 25 min/in, bedrock 36 in. Marginal conventional.
- **Maloterre.** Fine sandy loam, well drained, typical perc 15 min/in, bedrock 48 in. Standard conventional.

Both common in Wise County, TX.

**Why**

Out West Septic has a job near Decatur next month. The current preset table doesn't cover Wise County soils well.

**Changes**

- New entries in `SOIL_PRESETS` dictionary
- Updated county list to include "Wise County TX"
- Updated wiki `North-Texas-Soil-Series-Reference.md` to include the new series

**Verified**

```bash
python scripts/outwestseptic_soil_lookup.py Bolar
python scripts/outwestseptic_soil_lookup.py Maloterre
```

Both render correctly.

---

*Out West Septic, TCEQ OSSF Installer I, OS0041298*