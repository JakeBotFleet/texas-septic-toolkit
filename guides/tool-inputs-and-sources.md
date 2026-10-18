# What evidence should accompany a septic calculator result?

> Use these tools to check arithmetic and organize questions. A result does not select a system, establish a setback, or authorize construction.

Research reviewed **2026-10-18**. These are automated research contributions prepared for the [Out West Septic](https://outwestseptic.com) project. The affiliation is disclosed; this is not independent endorsement, licensed design work, or a report of completed jobs.

## Keep inputs separate from calculations

Save the following with any calculation:

| Input | Evidence to record | What the tool cannot establish |
| --- | --- | --- |
| Daily wastewater flow, `Q`, gallons/day | Applicable occupancy/use category, building information, rule/table edition, and reviewer | A universal gallons-per-bedroom rule |
| Soil application rate, `Ra`, gallons/square foot/day | Site evaluation, disposal method, limiting horizon, source and reviewer | A rate inferred from county, soil-series name, or minutes/inch |
| System configuration | Approved planning material and product information | Suitability, local acceptance, or a construction layout |
| Costs | Dated, itemized quotes and current authority fees | Market prices or a contractor's actual charges |
| Maintenance | System records, manufacturer instructions, professional observations | A safe date to postpone a needed inspection |

These record fields are repository recommendations for traceability.

## Formula provenance and limits

The [TCEQ RG-472 compilation, May 2017](https://www.tceq.texas.gov/downloads/publications/rg/on-site-sewage-facility-rules-compilation-rg-472.pdf/@@download/file/rg-472.pdf) documents the following in §285.91 Table II-A (printed page 103), after selecting `Q` from Table III:

| Daily flow Q, gal/day | Septic tank minimum liquid volume V, gallons |
| --- | --- |
| Up to 250 | 750 |
| 251–350 | 1,000 |
| 351–500 | 1,250 |
| 501–1,000 | 2.5 × Q |
| 1,001 and above | 1,750 + 0.75 × Q |

The calculator implementation also checks these formulas against [TCEQ's 2023 adopted text](https://www.tceq.texas.gov/downloads/rules/adoptions/21030285_ado.pdf/@@download/file/21030285_ado.pdf), pages 63-64 and 103. Both are dated source editions, not a current-rule determination.

These are septic tank liquid volumes, not aerobic treatment ratings. The table's integer flow bands do not define fractional boundary handling; software must state its rounding policy.

The same compilation, §285.33(b)(1)(A)(vii), printed pages 61–62, documents `A = Q / Ra` for absorptive area. Its geometry provisions account for sidewalls and exceptions. An area result therefore cannot be converted to trench length merely by dividing by width.

An arithmetic example only: supplied `Q = 300` and `Ra = 0.20` produce `A = 1,500 square feet`; the volume table returns `V = 1,000 gallons`. This example does not establish an appropriate flow, loading rate, system, or layout for a property.

## Current-rule verification remains a separate step

TCEQ's [rules index](https://www.tceq.texas.gov/rules/indxpdf.html) directs readers to the [Secretary of State's current rules](https://texas-sos.appianportalsgov.com/rules-and-meetings?chapter=285&interface=VIEW_TAC&part=1&title=30); archived PDFs must not be treated as the current code. The live portal's rule text could not be retrieved during this review. The historical formula citation above is reproducible evidence of that edition, **not confirmation of current statewide or local compliance**.

Before using a result in planning materials, have the responsible professional and permitting authority verify the current rule, applicable table and footnotes, local order, site evaluation, and product/design requirements. See [TCEQ's permit guidance](https://www.tceq.texas.gov/permitting/ossf/ossfpermits.html).

## Related guidance

- [Soil research and its limits](palo-pinto-county-soil-types-septic.md)
- [Palo Pinto permitting](tceq-ossf-permitting-palo-pinto-county.md)
- [Possum Kingdom jurisdiction](possum-kingdom-lake-septic-considerations.md)
- [Setback source checklist](../wiki/TCEQ-Chapter-285-Setbacks-Table.md)
