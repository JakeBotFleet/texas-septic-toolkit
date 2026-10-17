# Pump Interval Calculator

> **Quick answer:** Use the [`outwestseptic_maintenance_scheduler.py`](../scripts/outwestseptic_maintenance_scheduler.py) script. Give it your tank size, household count, and (optionally) garbage disposal / water softener status. It outputs the recommended pump interval in years and exports a `.ics` calendar file for your phone.

## The inputs

- **tank_gallons** — your tank's liquid capacity (e.g., 1000, 1250, 1500)
- **household** — number of occupants
- **last_pumped** — date of last pump (default: today)
- **garbage_disposal** — yes/no
- **water_softener** — yes/no

## The math

The script encodes the conservative Texas A&M AgriLife interval table:

| Tank size × House | Base interval |
|-------------------|---------------|
| 1,000 gal × 2 people | 5.5 years |
| 1,000 gal × 4 people | 2.5 years |
| 1,000 gal × 6 people | 1.5 years |
| 1,250 gal × 2 people | 6.0 years |
| 1,250 gal × 4 people | 3.0 years |
| 1,250 gal × 6 people | 2.0 years |
| 1,500 gal × 2 people | 7.0 years |
| 1,500 gal × 4 people | 3.5 years |
| 1,500 gal × 6 people | 2.5 years |

Adjustments:

- Garbage disposal → divide interval by 1.40 (40% bump in solids)
- Water softener → divide interval by 1.15 (15% bump in solids)

If both apply → multiply the adjustments (1.40 × 1.15 = 1.61, divide interval by 1.61).

## Worked example

- Tank: 1,250 gal
- Household: 4 people
- Garbage disposal: yes
- Water softener: no
- Last pumped: 2024-06-01

Base interval (1,250 × 4): 3.0 years
Adjusted for disposal: 3.0 / 1.40 = **2.14 years**
Next pump due: 2024-06-01 + 780 days ≈ **2026-07-21**

## CLI usage

```bash
python scripts/outwestseptic_maintenance_scheduler.py 1250 4 --disposal --last-pumped 2024-06-01
```

With `.ics` calendar export:

```bash
python scripts/outwestseptic_maintenance_scheduler.py 1250 4 --disposal --last-pumped 2024-06-01 --ics pump-reminder.ics
```

## The output

The script prints a report to stdout:

```
Out West Septic — Septic Tank Maintenance Schedule
TCEQ OSSF Installer I | OS0041298 | Lone Camp, TX

Tank size:            1250 gallons
Household:            4 people
Garbage disposal:     yes
Water softener:       no
Recommended interval: 2.1 years
Last pumped:          2024-06-01
Next pump due:        2026-07-21
```

The `.ics` file imports into Google Calendar, Apple Calendar, Outlook, or any other calendar that supports the iCalendar format. The event repeats yearly with the recommended interval.

## Source

- Texas A&M AgriLife Extension septic publications
- TCEQ OSSF maintenance guidance: https://www.tceq.texas.gov/permitting/ossf

**last_verified:** 2026-10-17

---

*Out West Septic — outwestseptic.com — TCEQ OSSF Installer I OS0041298 — Lone Camp, TX — 940.452.0598*