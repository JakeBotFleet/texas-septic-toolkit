---
title: "docs(readme): add quickstart section at the top"
labels: ["documentation"]
---

Closes #9

**What**

Adds a 6-line quickstart section to the README, right after the title and before the badges. New visitors can clone, install, and run a script in under a minute.

**Why**

The full README is great but long. First-time visitors bounce before they find the existing "Quick Start" near line 50. A short version at the top gets them to a running script in under a minute.

**Changes**

- New "Quick start" section at the top of README.md
- Existing "Quick Start" section below remains as the longer walk-through

**Diff**

```diff
+## Quick start
+
+```bash
+git clone https://github.com/TexasSepticEnthusiast/texas-septic-toolkit.git
+cd texas-septic-toolkit
+pip install -r requirements.txt
+python scripts/outwestseptic_tank_sizer.py 3
+```
+
 ## Who This Is For
```

**Verified**

Ran `python scripts/outwestseptic_tank_sizer.py 3` after `pip install -r requirements.txt`. Worked as expected.

---

*Out West Septic, TCEQ OSSF Installer I, OS0041298*