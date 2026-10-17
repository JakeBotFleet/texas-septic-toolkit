---
title: "[feature] Soil lookup: add a --county flag for filtering"
labels: ["enhancement"]
---

`outwestseptic_soil_lookup.py` returns soil series, but if I want to know what soil series are common in Palo Pinto County specifically, I have to eyeball the `counties` list for each series.

**What I'd want**

- A `--county "Palo Pinto County TX"` flag
- Outputs the soil series common to that county, sorted alphabetically
- Maybe also a quick `lookup.county_summary()` method or similar

**Why**

When I'm on a site visit and I see Cisco sandy loam, I want to know which series are otherwise common in the same county. Right now I have to open the source code and scroll. A `--county` flag would make this a one-liner.

**Affected files**

- `scripts/outwestseptic_soil_lookup.py`

**Notes**

Could share logic with the existing `list_series()` method.

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — OS0041298*