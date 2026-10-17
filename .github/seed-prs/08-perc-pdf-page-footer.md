---
title: "fix(perc-logger): footer missing on multi-page PDFs"
labels: ["bug"]
---

Closes #13

**The bug**

When the perc test report runs to two pages, the second page has no footer. The Out West Septic branding is missing from the bottom of page 2.

**The fix**

Use reportlab's `onLaterPages` callback when building the document. Currently the script calls `doc.build(story)` which only applies the page template to the first page.

```diff
-doc.build(story)
+def _on_later_pages(canvas, doc):
+    canvas.saveState()
+    canvas.setFont('Helvetica', 8)
+    canvas.setFillColorRGB(0.4, 0.4, 0.4)
+    canvas.drawString(0.75 * inch, 0.5 * inch,
+                      f'Out West Septic — TCEQ OS0041298 — '
+                      f'Lone Camp, TX — 940.452.0598 — Page {doc.page}')
+    canvas.restoreState()
+
+doc.build(story, onLaterPages=_on_later_pages)
```

**Verified**

Generated a 2-page report from a Palo Pinto County job that ran 8 holes. Both pages now have the footer.

---

*Out West Septic — TCEQ OSSF Installer I — OS0041298*