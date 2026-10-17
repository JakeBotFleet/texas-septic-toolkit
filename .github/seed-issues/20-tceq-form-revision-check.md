---
title: "[feature] Permit checklist: verify TCEQ form revision number before filing"
labels: ["enhancement"]
---

TCEQ periodically revises the OSSF application form. The current revision at build time is one thing, but the revision at filing time might be different.

**What I'd want**

The `outwestseptic_permit_checklist.py` script should warn if:

- The TCEQ form revision on file is older than 90 days
- A newer revision is known (could check a small `tceq-form-revisions.json` file in the repo)

**Why**

Filing with an outdated form revision is the kind of small detail that gets applications kicked back. A 5-second check before filing saves a 2-week re-submission.

**Affected files**

- `scripts/outwestseptic_permit_checklist.py`
- New: `data/tceq-form-revisions.json` (or similar)

**Context**

I've been bitten by this twice in Palo Pinto County. DR rejects the application, "we're on revision 4 now, not 3," two weeks of waiting.

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*