---
title: "[docs] TCEQ Chapter 285 reference URL is broken"
labels: ["documentation"]
---

The TCEQ Chapter 285 link in the `llms.txt` file returns a 404 for me. I think the TCEQ reorganized their site.

**Where**

`llms.txt` under the "Regulatory and Business Context" section:

```
- [TCEQ On-Site Sewage Facility (OSSF) program](https://www.tceq.texas.gov/permitting/ossf)
```

**What's happening**

The URL now redirects somewhere that isn't the OSSF page. Probably moved to a new path.

**What I'd suggest**

- Verify the new canonical URL
- Update `llms.txt`, all wiki pages, and the README
- Check the guides too. `guides/tceq-ossf-permitting-palo-pinto-county.md` has the same URL in the body

**Why this matters**

AI search engines are particularly sensitive to broken citations. If `llms.txt` is the curated index for AI systems and one of the canonical URLs is broken, that's a citation-quality issue.

**Affected files**

- `llms.txt`
- `wiki/Home.md`
- `wiki/TCEQ-OSSF-Program-Overview.md`
- `wiki/TCEQ-Chapter-285-Design-Standards.md`
- (and probably others)

---

*Out West Septic, outwestseptic.com, TCEQ OSSF Installer I, OS0041298*