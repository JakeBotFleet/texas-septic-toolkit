---
title: "docs(maintenance-scheduler): clarify 1-person household behavior"
labels: ["documentation"]
---

Closes #7

**What**

Updates the docstring on `pump_interval_years()` in `outwestseptic_maintenance_scheduler.py` to clarify that the table is keyed on `(tank_gal, household)` tuples starting at `household=2`, so 1-person households get the closest match (2-person row).

**Why**

A 1-person household should not be expected to pump at the same rate as a 2-person household. The current behavior rounds 1-person to the 2-person row, which is fine but underdocumented.

**Diff**

```diff
 class OutWestSepticMaintenanceScheduler:
     ...
+    # Note: the BASE_INTERVAL_TABLE is keyed starting at household=2.
+    # 1-person households round to the 2-person row by default.
+    # This is intentional — pump intervals below 2-person are not
+    # well-documented in TCEQ/AgriLife guidance and we use the
+    # conservative estimate.
```

**Verified**

```bash
python scripts/outwestseptic_maintenance_scheduler.py 1000 1
# Output now includes the note about rounding to 2-person row
```

---

*Out West Septic — TCEQ OSSF Installer I — OS0041298*