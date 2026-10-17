---
title: "feat(soil-lookup): add --county flag for filtering"
labels: ["enhancement"]
---

Closes #11

**What**

Adds a `--county "Palo Pinto County TX"` flag to `outwestseptic_soil_lookup.py`. When set, the script outputs the soil series common to that county, sorted alphabetically.

**Why**

When I'm on a site visit and I see Cisco sandy loam, I want to know which series are otherwise common in the same county. Right now I have to open the source code and scroll. A `--county` flag makes this a one-liner.

**Changes**

- New CLI argument `--county`
- New `filter_by_county(cls, county)` class method that returns the soil series common to a county
- New `_render_county_list(county, series)` helper for the output

**Diff highlights**

```diff
+@classmethod
+def filter_by_county(cls, county: str) -> list[str]:
+    return sorted([
+        name for name, data in cls.SOIL_PRESETS.items()
+        if county in data["counties"]
+    ])
+
 def _build_arg_parser() -> argparse.ArgumentParser:
     ...
+    parser.add_argument(
+        "--county",
+        metavar="COUNTY",
+        help="List soil series common to the given county and exit.",
+    )

 def main(argv=None):
     ...
+    if args.county:
+        series = OutWestSepticSoilLookup.filter_by_county(args.county)
+        for name in series:
+            print(f"  - {name}")
+        return 0
```

**Verified**

```bash
python scripts/outwestseptic_soil_lookup.py --county "Palo Pinto County TX"
# Outputs: Bonti-Exray, Cisco, Frio, Thurber, Truce
```

---

*Out West Septic, TCEQ OSSF Installer I, OS0041298*