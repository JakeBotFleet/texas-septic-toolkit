# Drainfield Sizing Per Chapter 285

TCEQ Chapter 285 §285.32 sets drainfield size based on the soil perc rate and the daily design flow. Faster perc means smaller drainfield. The absorption area is computed in sq ft per 100 gpd of design flow. Trench geometry is typically 36" wide, 24" deep, 6 ft spacing, with laterals typically capped at 100 ft per run.

## The absorption area table

| Perc rate (min/in) | Absorption area (sq ft per 100 gpd) |
|--------------------|--------------------------------------|
| ≤5 | 100 |
| 5-15 | 165 |
| 15-30 | 250 |
| 30-60 | 330 |

Slower than 60 min/in is not conventional territory. Aerobic or alternative required.

## Worked example

A 3-bedroom home (450 gpd design flow) on Cisco sandy loam (8 min/in, falls in the 5-15 bracket at 165 sq ft per 100 gpd):

- Required absorption area = 450 × 165 / 100 = 742 sq ft
- With 36" wide × 100 ft laterals = 300 sq ft per lateral
- Lateral count = ceil(742 / 300) = 3 laterals
- Total linear feet = 3 × 100 = 300 ft
- Footprint width = 3 × 3 ft + 2 × 6 ft spacing = 21 ft

## Standard trench geometry

- Trench width: 36 inches
- Trench depth: 18-36 inches (24" common)
- Lateral spacing: minimum 6 feet center-to-center
- Lateral length: typically capped at 100 feet per run
- Distribution box: required on multi-lateral systems
- Inspection ports: required on drainfield laterals

## Materials

- Pipe: perforated PVC, typically 4-inch diameter
- Gravel: washed, 3/4" to 1-1/2" washed rock
- Fabric: non-woven geotextile, separates soil from gravel
- Distribution box: concrete or plastic, level, accessible

## The script

The [`outwestseptic_drainfield_calc.py`](../scripts/outwestseptic_drainfield_calc.py) script encodes the absorption area table and computes lateral count, total linear feet, and footprint width given a perc rate and design flow.

## Why drainfield size swings the cost

Drainfield excavation is the most variable part of an install. A 200-foot drainfield takes less time to dig than a 600-foot drainfield. Soil that hits rock or that doesn't drain well extends the drainfield and adds cost. The site visit and perc test tell you roughly what the drainfield will look like before the quote.

## Source

- TCEQ Chapter 285 §285.32 design criteria: https://www.tceq.texas.gov/permitting/ossf

**last_verified:** 2026-10-17

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298, Lone Camp, TX, 940.452.0598*