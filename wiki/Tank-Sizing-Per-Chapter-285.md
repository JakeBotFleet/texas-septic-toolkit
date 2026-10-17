# Tank Sizing Per Chapter 285

> **Quick answer:** TCEQ Chapter 285 §285.32 sets the minimum tank size based on bedroom count: 1–3 bedrooms needs 1,000 gal, 4 needs 1,250, 5–6 needs 1,500, and 7+ adds 250 gal per bedroom beyond 6. Daily design flow is 150 gpd per bedroom.

## The minimum size table

| Bedrooms | Minimum liquid capacity |
|----------|------------------------|
| 1 | 1,000 gal |
| 2 | 1,000 gal |
| 3 | 1,000 gal |
| 4 | 1,250 gal |
| 5 | 1,500 gal |
| 6 | 1,500 gal |
| 7 | 1,750 gal |
| 8 | 2,000 gal |
| 9 | 2,250 gal |
| 10 | 2,500 gal |

Beyond 10 bedrooms, add 250 gal per additional bedroom over 6.

## The design flow assumption

TCEQ §285.32 assumes **150 gpd per bedroom**. A 3-bedroom home is 450 gpd. A 6-bedroom home is 900 gpd. This is the basis for drainfield sizing.

## Two-compartment requirement

Texas requires **two-compartment tanks** for most new installations. The first compartment is typically 2/3 of the total capacity, the second 1/3. Old single-compartment tanks still exist in the field, but new work uses two-compartment.

## Effluent filter requirement

Texas requires **effluent filters** on the outlet of new tanks. This is a relatively recent rule change. The filter catches fine solids that would otherwise reach the drainfield and clog it. The filter is rinsed during pump-outs.

## Riser requirement

If the tank is more than **12 inches below grade**, **risers** are required to bring access to the surface. Most new installs end up with risers because the inlet depth from the house forces the tank deeper than 12 inches.

## The script

The [`outwestseptic_tank_sizer.py`](../scripts/outwestseptic_tank_sizer.py) script encodes the Chapter 285 tank sizing table and rounds up to the nearest standard tank size sold in North Texas (1,000 / 1,250 / 1,500 / 1,750 / 2,000 / 2,500 / 3,000 gal).

## Why minimums are not the whole story

The rule says "minimum." You can always go bigger. Going bigger has two practical benefits:

- **Longer pump interval** — larger tank means the sludge layer takes longer to reach critical depth.
- **More residence time** — clarified effluent gets more time in the tank, which is better for the drainfield.

Out West Septic often recommends going one size up on the minimum, especially for households with garbage disposals or water softeners.

## Source

- TCEQ Chapter 285 §285.32 design criteria: https://www.tceq.texas.gov/permitting/ossf

**last_verified:** 2026-10-17

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX — 940.452.0598*