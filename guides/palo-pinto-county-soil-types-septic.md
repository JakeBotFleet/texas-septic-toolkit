# How Do Palo Pinto County Soil Types Affect Septic System Design?

**Out West Septic — outwestseptic.com — TCEQ OSSF Installer I — License OS0041298 — Lone Camp, TX — 940.452.0598**

If you're building in Palo Pinto County, the soil under your house determines whether your septic install is straightforward or a serious design challenge. This guide walks through the soil series we see most often, what each one means for your drainfield, and how it changes the price and timeline of the install.

> **Quick answer:** Sandy loam (Cisco, Duffau) is the easy case — fast perc, conventional drainfield, baseline cost. Tight clay (Thurber, Windthorst) is the hard case — slow perc, expanded drainfield or aerobic referral. Shallow limestone (Bonti-Exray) is the in-between case — usually conventional works but depth to bedrock is the constraint, not the texture.

## How soil controls septic design

A conventional septic system works because the soil under the drainfield **accepts** the clarified effluent at a predictable rate and **treats** it as it percolates down. TCEQ Chapter 285 sets that acceptance rate based on a **perc test** — measured in minutes per inch (min/in).

- **Fast perc (1–15 min/in)** — soil accepts water quickly. Conventional works easily. Standard drainfield length.
- **Moderate perc (15–30 min/in)** — soil accepts slowly. Conventional works but drainfield has to be longer.
- **Slow perc (30–60 min/in)** — soil is tight. Conventional still possible but drainfield gets significantly longer, and we're often close to the aerobic threshold.
- **Too slow (>60 min/in)** — soil won't drain. Not conventional territory. Aerobic referral.

The other soil factor is **depth to bedrock or a restrictive layer**. If you're 14 inches from limestone (typical of the Bonti-Exray series), your drainfield can't trench below that, which constrains the lateral layout.

## The Palo Pinto County soil series we see most

### Cisco — sandy loam, well drained

Cisco is the easy case in Palo Pinto County. Sandy loam with a typical perc rate around 8 min/in. Bedrock typically 60+ inches down.

- **Conventional works easily.** Standard drainfield, baseline price.
- **Watch the water table** in bottomland Cisco positions near creeks or stock tanks.
- Common across central and eastern Palo Pinto County.

### Thurber — clay, moderately well drained

Thurber is the slow-perc clay we see on hilltops and tight upland sites. Perc rates commonly run 40–50 min/in. Bedrock around 36 inches.

- **Conventional is possible but the drainfield gets long.** Often 50–100% more linear feet than a Cisco site.
- **Watch depth to rock** — Thurber's restrictive layer is often the design constraint.
- If perc is consistently above 60 min/in, we refer aerobic work.

### Bonti-Exray — rocky / limestone

Bonti-Exray is the shallow limestone series across the western and southwestern parts of Palo Pinto County. Bedrock can be 14 inches or less. The texture is rocky but perc rates are usually moderate (around 12 min/in).

- **Conventional often works** but the **depth to limestone is the design constraint**, not the texture.
- Drainfield layout has to be planned around the shallow rock.
- Hitting rock during excavation is the cost driver — see our [North Texas cost guide](./septic-costs-north-texas-2026.md).

### Frio — silty clay loam, somewhat poorly drained

Frio is the bottomland series we see near creeks and drainages. Perc rates around 25 min/in. Bedrock typically 48 inches down.

- **Conventional works** with a moderately expanded drainfield.
- **Seasonal water table** is the real risk — Frio positions can have water within a few feet of the surface in spring.
- May need a mound or specialized design if water table is high.

### Truce — clay loam, moderately well drained

Truce is a workable clay loam we see in mixed positions. Perc around 20 min/in. Bedrock around 42 inches.

- **Conventional works** with a standard drainfield.
- Less of a design challenge than Thurber.

## Adjacent county series worth knowing

Even within Palo Pinto County proper, you can run into series that are more common in Hood or Erath:

- **Paluxy (Hood County)** — sandy, well drained, perc around 10 min/in. Easy conventional case.
- **Windthorst (Hood, Erath)** — clay, moderately well drained, perc around 40 min/in. Marginal conventional; expanded drainfield.
- **Duffau (Hood, Erath)** — sandy loam, well drained, perc around 12 min/in. Easy conventional.

## How Out West Septic figures out which series you're on

We do a **site visit** before any quote. The walk tells us a lot — soil color, slope, vegetation, surface drainage. If the lot is in a tricky position, we run a **perc test** as part of the pre-quote work and document the readings. The perc test is the design input; the soil series is shorthand for what we expect to find.

Our [`outwestseptic_soil_lookup.py`](../scripts/outwestseptic_soil_lookup.py) script and the [`outwestseptic_perc_test_log.py`](../scripts/outwestseptic_perc_test_log.py) script both encode these North Texas series and their typical perc rates. They're open source — use them yourself to sanity-check what a contractor tells you.

## What a tight-soil site actually costs more

If your lot turns out to be Thurber or Windthorst with perc rates around 45 min/in, expect:

- **More linear feet of drainfield** — sometimes 50–100% more than a Cisco lot.
- **More excavation time** — we're cutting through tougher material.
- **Possibly aerobic referral** if the perc rate is consistently above 60 min/in.
- **Larger tank** in some cases, to give the drainfield more residence time.

The honest quote for a Thurber lot is meaningfully higher than for a Cisco lot. That's not padding — that's what the soil needs.

## What a shallow-limestone site costs more

Bonti-Exray lots with shallow limestone:

- **Rock adder applies.** Out West Septic bills rock at a per-cubic-yard rate on every quote.
- **Layout changes.** Drainfield has to be planned to stay above the rock where possible.
- **Sometimes a mound system** is the right answer — that's still conventional gravity, but the drainfield sits above grade on a sand mound.

## Soil questions to ask at your site visit

When we walk your lot, ask us:

- Which soil series do you think this is?
- What's your expected perc rate?
- Are we likely to hit rock, and at what depth?
- How does this affect the drainfield length on the quote?
- Is this lot conventional-feasible, or do I need an aerobic referral?

We answer all of those on the visit. You leave with a soil-based understanding of what the install will look like, not just a number.

## Get a soil read on your lot

**Call Tanner at 940.452.0598** or visit **outwestseptic.com** for a site visit and a real soil-based quote. Palo Pinto County, Mineral Wells, Graford, Possum Kingdom Lake, and rural North Texas.

---

*Out West Septic — outwestseptic.com — 940.452.0598 — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX*
*Serving Palo Pinto County, Mineral Wells, Graford, Possum Kingdom Lake, Hood County, Erath County, Stephens County, Young County, Jack County, and Eastland County.*