---
title: "[question] What happens if the perc rate is exactly 60 min/in?"
labels: ["question"]
---

Reading through `outwestseptic_drainfield_calc.py` and the absorption area table, the boundary case at 60 min/in is interesting.

The table goes `≤5, 5-15, 15-30, 30-60`, with the 30-60 bracket at 330 sq ft per 100 gpd. The `absorption_area_sqft` function uses `<=` for the upper bound, so 60 min/in exactly would fall into the 30-60 bracket (330 sq ft per 100 gpd).

But the classify function in `outwestseptic_perc_test_log.py` has `> 60` as the threshold for "TOO SLOW — not conventional territory."

So a perc rate of exactly 60.0 min/in would pass the drainfield calc but get classified as "TOO SLOW" by the perc logger. That's inconsistent.

**Why I'm asking**

I had a perc test last week that came back at 59.8 min/in (close to the boundary). The drainfield calc said conventional was fine. The perc logger classified it as "VERY SLOW — borderline conventional." Both responses are arguably correct, but they're describing the same number differently.

**Question**

Should the classification thresholds in `outwestseptic_perc_test_log.py` use `>=` instead of `>` for the 60 min/in cut? Or should the absorption table in `outwestseptic_drainfield_calc.py` use a different cut? TCEQ §285.32 doesn't pin this down to a specific minute, but the two scripts should be consistent.

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*