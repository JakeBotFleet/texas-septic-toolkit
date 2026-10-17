# Maintenance Schedule for Homeowners

> **Quick answer:** Pump your septic tank every 3 to 5 years. Don't flush wipes. Don't pour grease down the drain. Spread laundry over the week. Get an inspection every 2–3 years. Out West Septic does not run a pump truck — we refer pumping to local pumpers.

## The pump interval

| Tank size | Household | Pump interval |
|-----------|-----------|---------------|
| 1,000 gal | 2 people | ~5 years |
| 1,000 gal | 4 people | ~2–3 years |
| 1,000 gal | 6 people | ~1.5–2 years |
| 1,250 gal | 2 people | ~6 years |
| 1,250 gal | 4 people | ~3 years |
| 1,250 gal | 6 people | ~2 years |
| 1,500 gal | 2 people | ~7 years |
| 1,500 gal | 4 people | ~3.5 years |
| 1,500 gal | 6 people | ~2.5 years |

Add a garbage disposal → knock 30–40% off.
Add a water softener → knock another 10–15% off.

## What NOT to do

- **Don't flush wipes** — even "flushable" wipes don't break down
- **Don't pour grease down the drain** — solidifies in the tank
- **Don't use the disposal as a trash can** — every load becomes solids in the tank
- **Don't do all your laundry in one day** — large water slug stirs the tank
- **Don't park or drive over the tank or drainfield**
- **Don't plant trees near the drainfield**
- **Don't direct roof gutters over the drainfield**
- **Don't use harsh chemical drain cleaners**

## What TO do

- **Spread laundry over the week**
- **Fix leaks promptly**
- **Use septic-safe toilet paper**
- **Keep a record of pump dates**
- **Get an inspection every 2–3 years** — Out West Septic charges $250–$500
- **Install risers if your tank doesn't have them**

## Signs your tank is overdue

- Slow drains throughout the house
- Gurgling sounds in plumbing
- Sewer odor in the house or yard
- Wet spots over the drainfield
- Backups in the lowest drains

If you see any of these, get the tank pumped first. If pumping doesn't fix it, the next step is a drainfield inspection.

## The TCEQ rule of thumb

The TCEQ and Texas A&M AgriLife both recommend pumping **at least every 3 to 5 years** for a conventional system serving a typical household. That's the public-facing guidance.

## The script

The [`outwestseptic_maintenance_scheduler.py`](../scripts/outwestseptic_maintenance_scheduler.py) script calculates your specific interval based on tank size and household, then exports a `.ics` calendar file so you can put the next pump on your phone.

## Source

- TCEQ homeowner maintenance guidance: https://www.tceq.texas.gov/permitting/ossf
- Texas A&M AgriLife Extension septic publications

**last_verified:** 2026-10-17

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX — 940.452.0598*