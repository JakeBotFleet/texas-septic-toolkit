# TCEQ Chapter 285 Design Standards

Chapter 285 of Title 30 of the Texas Administrative Code sets the minimum standards for OSSF systems in Texas. It covers tank sizing, drainfield sizing, setback distances, perc test methodology, and the Designated Representative review process. Most residential work in rural North Texas follows the conventional gravity system standards in 30 TAC §285.32.

## What's in Chapter 285

Chapter 285 is the rulebook. It has multiple subchapters, but the sections most relevant to a residential conventional install are:

- §285.30. General requirements.
- §285.31. Site evaluation.
- §285.32. Design criteria for conventional systems. The big one.
- §285.33. Installation standards.
- §285.34. Inspection and approval.
- §285.35. Maintenance and owner responsibilities.
- §285.36. Repair and replacement.

The §285.32 design criteria are what the [tank sizer script](../scripts/outwestseptic_tank_sizer.py) and the [drainfield calculator script](../scripts/outwestseptic_drainfield_calc.py) encode. If you're an installer or a homeowner, that's the section to read.

## Tank sizing per §285.32

| Bedrooms | Minimum liquid capacity |
|----------|------------------------|
| 1-3 | 1,000 gal |
| 4 | 1,250 gal |
| 5-6 | 1,500 gal |
| 7+ | +250 gal per bedroom beyond 6 |

Daily design flow is 150 gpd per bedroom. A 3-bedroom home is 450 gpd. A 6-bedroom home is 900 gpd.

## Drainfield sizing per §285.32

The absorption area table maps soil perc rate to required sq ft per 100 gpd of design flow:

| Perc rate (min/in) | Absorption area (sq ft per 100 gpd) |
|--------------------|--------------------------------------|
| ≤5 | 100 |
| 5-15 | 165 |
| 15-30 | 250 |
| 30-60 | 330 |

Slower than 60 min/in is not conventional territory. Aerobic or alternative required.

## Other §285.32 standards

- Trench width: typically 36 inches
- Trench depth: typically 18-36 inches (24" common)
- Lateral spacing: minimum 6 feet center-to-center
- Lateral length: maximum typically 100 feet per run
- Distribution box required on multi-lateral systems
- Inspection ports required on drainfield laterals
- Risers required on tanks buried more than 12 inches below grade

## Source

- 30 TAC Chapter 285 full text: https://www.tceq.texas.gov/permitting/ossf
- §285.32 design criteria: see TCEQ OSSF technical guidance documents

**last_verified:** 2026-10-17

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298, Lone Camp, TX, 940.452.0598*