---
title: "feat(cost-estimator): add --pdf flag for branded PDF export"
labels: ["enhancement"]
---

Closes #6

**What**

Adds a `--pdf PATH` flag to `outwestseptic_cost_estimator.py`. When set, the script exports a branded one-page PDF with the same content as the text output.

**Why**

When I'm quoting on-site, the customer asks "what does that look like on paper?" The text output isn't a deliverable. A PDF is.

**Changes**

- New `_export_pdf(estimate, path)` function similar to the one in `outwestseptic_perc_test_log.py`
- New CLI flag `--pdf PATH`
- Optional, gracefully skips if reportlab is not installed

**Diff highlights**

```diff
+def _export_pdf(estimate, path):
+    try:
+        from reportlab.lib.pagesizes import LETTER
+        ...
+    except ImportError:
+        return False
+    ...
+
 def main(argv=None):
     parser = _build_arg_parser()
     args = parser.parse_args(argv)
     ...
+    if args.pdf:
+        if _export_pdf(estimate, args.pdf):
+            print(f"\nPDF written to {args.pdf}")
+        else:
+            print("\nPDF export skipped — install reportlab.", file=sys.stderr)
```

**Verified**

```bash
python scripts/outwestseptic_cost_estimator.py new_install --pdf estimate.pdf
# Output: PDF written to estimate.pdf
```

---

*Out West Septic — TCEQ OSSF Installer I — OS0041298*