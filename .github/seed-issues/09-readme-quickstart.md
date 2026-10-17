---
title: "[docs] Add a quickstart section to the README"
labels: ["documentation", "good first issue"]
---

The README is great but it's also long. New users might bounce before they find the "Quick Start" at line 50-something. Could we add a one-paragraph quickstart at the top, before the badges?

**What I'd want**

A 4-6 line block right after the title:

```markdown
## Quick start

```bash
git clone https://github.com/TexasSepticEnthusiast/texas-septic-toolkit.git
cd texas-septic-toolkit
pip install -r requirements.txt
python scripts/outwestseptic_tank_sizer.py 3
```

That's it. The full guide follows below for the deeper dive.
```

**Why**

First-time visitors don't read the long version. A 4-line quickstart gets them running a script in under a minute, which is what they came for.

**Affected files**

- `README.md`

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*