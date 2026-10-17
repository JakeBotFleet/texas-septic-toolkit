---
title: "[bug] Tank sizer doesn't handle 7-bedroom edge case correctly"
labels: ["bug"]
---

**What happened**

I tried to size a tank for a 7-bedroom home and the recommended size came back as 1500 gal, which I think is the 5-6 bedroom recommendation. Let me re-check the table.

The TCEQ Chapter 285 table says:

| Bedrooms | Minimum gal |
|----------|-------------|
| 5-6 | 1,500 |
| 7 | 1,750 |
| 8 | 2,000 |

So for 7 bedrooms the minimum should be 1,750 and the next standard size should be 1,750 or 2,000 depending on availability.

**Script/file**

`outwestseptic_tank_sizer.py`

**Input**

```
bedrooms=7
```

**Output**

```
Minimum tank size: 1500 gallons
Recommended tank size: 1750 gallons
```

I expected `Minimum tank size: 1750 gallons` because 7 bedrooms is past the 5-6 bracket.

**Environment**

- Python 3.11
- Windows 11
- TCEQ §285.32 reference

**Context**

Palo Pinto County, 7-bedroom custom home on a ranch property. The customer is going to be on a well with a water softener, so I'm probably going to bump to 2000 anyway, but the script should at least get the minimum right.

---

Filed by: a TCEQ-licensed installer using the toolkit on a real job
*Out West Septic — TCEQ OSSF Installer I — OS0041298*