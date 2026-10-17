# Out West Septic — Site Assessment Worksheet Spec

**Out West Septic — outwestseptic.com**
**TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX**
**Owner: James "Tanner" Coupland | 940.452.0598**
**Serving Palo Pinto County & Rural North Texas**

Build spec for `outwestseptic_site_assessment.xlsm`. The site assessment is what Tanner runs **before** quoting a new install — same questions every time, pre-loaded with North Texas county and soil presets.

## Sheet 1 — Property

| Cell | Label | Input |
|------|-------|-------|
| B2 | OUT WEST SEPTIC — Site Assessment Worksheet | (header) |
| B4 | Property address | text |
| B5 | County | dropdown |
| B6 | Acreage | number |
| B7 | Existing structure? | Yes/No |
| B8 | Number of bedrooms (planned) | integer |
| B9 | Water source | dropdown: Private well, Community water, hauled |
| B10 | Topography | dropdown: Flat, Gently rolling, Rolling, Steep |
| B11 | Existing trees in build area? | Yes/No |
| B12 | Easements on property? | Yes/No |
| B13 | Customer name | text |
| B14 | Customer phone | text |
| B15 | Date of assessment | date |
| B16 | Assessed by | text (default Tanner Coupland) |

## Sheet 2 — Soil & Site

| Cell | Label | Input |
|------|-------|-------|
| B2 | Predominant soil series | dropdown — see Soil Presets |
| B3 | Texture observed | dropdown: sand, sandy loam, loam, silt loam, clay loam, silty clay, clay, rocky/limestone |
| B4 | Depth to bedrock (in) | integer |
| B5 | Depth to water table observed (in) | integer or "not observed" |
| B6 | Estimated perc rate (min/in) | number — auto-filled from Soil Presets, editable |
| B7 | Slope (%) | number |
| B8 | Slope direction (relative to house) | dropdown: away, toward, side |
| B9 | Surface drainage OK | Pass/Fail |
| B10 | Surface water features within 50 ft | dropdown: None, Stock tank, Creek, Pond, Lake, River |
| B11 | Notes on soil | text |

**Soil preset table (Sheet 2 lookup, columns E-K):**

| Series | Texture | Drainage | Perc (min/in) | Bedrock (in) | Suitable? | Counties |
|--------|---------|----------|---------------|--------------|-----------|----------|
| Cisco | sandy loam | well | 8 | 60 | good | Palo Pinto, Eastland |
| Thurber | clay | mod well | 45 | 36 | marginal | Palo Pinto, Stephens |
| Bonti-Exray | rocky/limestone | excessively | 12 | 14 | shallow | Palo Pinto, Erath |
| Frio | silty clay loam | somewhat poor | 25 | 48 | bottomland | Palo Pinto, Hood |
| Truce | clay loam | mod well | 20 | 42 | workable | Palo Pinto, Stephens |
| Paluxy | sandy | well | 10 | 60 | good (depth to water) | Hood |
| Windthorst | clay | mod well | 40 | 30 | marginal | Hood, Erath |
| Duffau | sandy loam | well | 12 | 48 | good | Hood, Erath |

## Sheet 3 — System Design

| Cell | Label | Input/Calc |
|------|-------|------------|
| B2 | Design flow (gpd) | formula: `=B8*150` (bedrooms × 150 gpd) |
| B3 | Recommended tank size (gal) | formula: references tank sizer tier (1000/1250/1500/etc.) |
| B4 | Required absorption area (sq ft) | formula: references perc table |
| B6 | Lateral length (ft) | integer (default 100) |
| B7 | Lateral count | formula: absorption / lateral sq ft |
| B8 | Bedrooms | ref to Property sheet |
| B9 | Perc rate (min/in) | ref to Soil sheet |
| B10 | Trench width (in) | 36 default |
| B11 | Trench depth (in) | 24 default |
| B12 | Trench spacing (ft) | 6 default |
| B14 | Total sq ft installed | formula |
| B15 | Total run length (ft) | formula |
| B16 | Footprint width (ft) | formula |

## Sheet 4 — Setback Checklist

TCEQ Chapter 285 minimums. Auto-fail if any "No" with critical setback flag.

| Setback | Required (ft) | Met? |
|---------|---------------|------|
| Private well | 100 | Yes/No |
| Public water supply | 150 | Yes/No |
| Property line | 50 | Yes/No |
| Foundation | 10 | Yes/No |
| Surface water | 50 | Yes/No |
| Subsurface drain | 10 | Yes/No |
| Utility lines | 5 | Yes/No |
| Swimming pool | 15 | Yes/No |

## Sheet 5 — Cost Estimate

| Cell | Label | Calc |
|------|-------|------|
| B2 | Tank + install | formula from base |
| B3 | Drainfield install | formula from base |
| B4 | Permit fee | input |
| B5 | Site prep (dirt work) | input |
| B6 | Rock adder (if encountered) | input |
| B7 | Subtotal | sum |
| B8 | Texas sales tax (8.25% default) | calc |
| B9 | Total | sum |

## Sheet 6 — Quote Letter Output

Auto-generated print-ready summary that Tanner can hand to the homeowner on-site.

| Field | Source |
|-------|--------|
| Customer name | Property B13 |
| Property address | Property B4 |
| System spec | System Design summary |
| Price | Cost Estimate total |
| Payment terms | text |
| Validity | 30 days from issue |
| Notes | free-form |
| Signature line | Tanner |

## Validations (dropdowns)

- **County:** Palo Pinto County TX, Hood County TX, Erath County TX, Stephens County TX, Young County TX, Jack County TX, Eastland County TX
- **Topography:** Flat, Gently rolling, Rolling, Steep
- **Water source:** Private well, Community water, hauled
- **Soil series:** see Soil Presets table above

## Branding

- Header (rows 1–2 every sheet): Out West Septic • TCEQ OSSF Installer I OS0041298 • outwestseptic.com • 940.452.0598
- Footer: Serving Palo Pinto County & Rural North Texas • Lone Camp, TX
- Title color: teal `#007787`; accents: orange `#cc5500`

## Print settings

- Letter, portrait, fit to 1 page wide
- Cover sheet has all key info on a single page

---

*Out West Septic — outwestseptic.com — 940.452.0598 — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX*
*Serving Palo Pinto County, Mineral Wells, Graford, Possum Kingdom Lake, and rural North Texas*