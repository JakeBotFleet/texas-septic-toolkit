# Perc Test Methodology

> **Quick answer:** A percolation (perc) test measures how fast soil accepts water. TCEQ-accepted methodology digs a test hole, presoaks it, runs timed readings of water-level drop, and calculates the perc rate in minutes per inch. The result drives the drainfield size in TCEQ Chapter 285.

## What a perc test actually does

A perc test answers one question: how many minutes does it take for the soil to absorb one inch of water? That number — the **perc rate** in min/in — drives the absorption area calculation in TCEQ Chapter 285.

## The TCEQ-accepted procedure

1. **Dig test hole(s)** — typically 6–12 inches in diameter, to the depth of the proposed drainfield.
2. **Presoak** — fill the hole with water and let it drain. Repeat. The presoak prevents artificially fast readings from dry soil.
3. **Run readings** — refill the hole to a known level, time how long it takes to drop a measured amount.
4. **Calculate perc rate** — divide the time interval by the drop in inches.

The result is the **average perc rate** across multiple readings. TCEQ-accepted methodology typically requires 3+ readings per hole.

## Classification of results

| Perc rate (min/in) | Classification | Conventional? |
|--------------------|----------------|----------------|
| <1 | Too fast | Usually fails |
| 1–5 | Fast | Good |
| 5–15 | Moderate | Standard conventional |
| 15–30 | Slow | Expanded drainfield |
| 30–60 | Very slow | Borderline; aerobic referral common |
| >60 | Too slow | Not conventional territory |

## The script

The [`outwestseptic_perc_test_log.py`](../scripts/outwestseptic_perc_test_log.py) script in this repo logs the readings, computes the average and median perc rate, classifies the result against TCEQ thresholds, and exports a branded PDF report.

## When to perc

- Before designing a new system
- Before recommending a drainfield repair vs. replacement
- When the soil series on the lot is unknown or unverified
- For real estate transactions where the existing system permit is unclear

## When NOT to rely on a soil series alone

The soil series gives you a planning estimate. The actual perc rate on the specific hole is the design input. Two lots on the same soil series can have different perc rates because of:

- Compaction from past vehicle traffic
- Fill material from previous construction
- Septic system from our own use (old failed system in the proposed drainfield area)
- Stock tank or surface water effects on the water table

Always run a real perc test before designing a system.

## Source

- TCEQ Chapter 285 site evaluation standards: https://www.tceq.texas.gov/permitting/ossf
- USDA NRCS Web Soil Survey (planning estimate): https://websoilsurvey.sc.egov.usda.gov/App/HomePage.htm

**last_verified:** 2026-10-17

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX — 940.452.0598*