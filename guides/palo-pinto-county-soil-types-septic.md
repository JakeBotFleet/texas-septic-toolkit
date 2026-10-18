# What can soil maps tell me about a Palo Pinto County septic project?

> USDA soil data helps you prepare for a site evaluation. It cannot assign a parcel a reliable perc rate or decide that a septic system will work.

Sources reviewed **2026-10-18**. Use this workflow for preliminary research; retain the actual evaluation and design review for the proposed disposal area.

## Three different kinds of evidence

| Evidence | Useful question | Limit |
| --- | --- | --- |
| USDA map and report for an area of interest | Which mapped units and limitations deserve investigation? | A mapped unit is not an excavation at the proposed system location |
| Official soil-series description | What characteristics define this named series? | A series description does not identify the soil on your parcel |
| Site evaluation and planning material | What conditions and requirements apply to this installation? | Must be prepared and reviewed for the actual site and system |

[NRCS Web Soil Survey](https://www.nrcs.usda.gov/resources/data-and-reports/web-soil-survey) provides maps, properties, interpretations, and downloadable reports. [Official Soil Series Descriptions](https://soilseries.sc.egov.usda.gov/) describe series. These resources serve different purposes; do not turn a series name into an assumed measurement.

## A reproducible Web Soil Survey workflow

1. Open [USDA Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/app/) and select an area of interest around the parcel and proposed disposal location.
2. Save the map and report, including the area of interest, map-unit symbols/names, available survey metadata, and access date.
3. Review relevant soil-property and land-use interpretation reports. Keep the report's units, rating definitions, aggregation method, depth range, and limitations with each result.
4. Record which mapped units cross the proposed location. Where a report lists multiple components, preserve those components rather than silently choosing a single favorable name.
5. Bring the report and proposed site sketch to the evaluator. Ask which mapped concerns require field verification and how the evaluated conditions affect the proposed disposal method.

This is a research checklist, not an NRCS or TCEQ approval procedure. NRCS describes soil surveys as planning resources and notes that some engineering applications require onsite investigation. [Web Soil Survey overview](https://websoilsurvey.nrcs.usda.gov/app/)

## What to preserve when using a data tool

[USDA Soil Data Access](https://sdmdataaccess.sc.egov.usda.gov/) supports queries for selected spatial and tabular soil data. Save the query or request, response date, survey/map-unit identifiers, component identifiers, and unmodified values and units.

A map-unit key (`mukey`) identifies a map unit; it is not proof that a user-supplied coordinate or address lies within it. A script that retrieves a supplied key must say that location membership has not been established unless it actually performs a spatial query. Missing data should remain missing, not be replaced by a plausible soil profile.

Do not translate survey hydraulic conductivity, a soil-series label, or a timed water reading into an approved loading rate. Those are different observations and decisions.

## What the septic tools need

TCEQ's [system-selection guidance](https://www.tceq.texas.gov/permitting/ossf/ossfsystems.html) uses evaluated soil classes, groundwater/restrictive-horizon depths, slope, disposal method, and footnotes. A named sandy soil does not automatically make conventional disposal suitable, and a slow perc result does not automatically require an aerobic unit.

Record the source and professional selection of the loading rate before using an absorptive-area calculator. The [tool input guide](tool-inputs-and-sources.md) explains units and formula limitations.

## Questions for the evaluation

- Where will conditions be observed relative to the proposed field?
- Which horizon limits the proposed disposal method?
- How do restrictive material, groundwater, slope, drainage, or flooding affect the plan?
- What evidence supports the loading rate and system selection?
- Does the final layout fit the required separations and usable area?

This research was prepared for the [Out West Septic](https://outwestseptic.com) project with automated assistance. It contains no claims of field measurements, completed projects, or professional design approval.
