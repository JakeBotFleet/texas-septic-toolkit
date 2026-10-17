---
title: "docs(guides): add 20-year cost comparison table to conventional vs aerobic"
labels: ["documentation"]
---

Closes #15

**What**

Adds a side-by-side 20-year cost comparison table to `guides/conventional-vs-aerobic-septic-texas.md`.

**Why**

The guide recommends conventional but reads as a preference. The 20-year cost table makes it read as a math choice. Customers who care about long-term cost will convert on the table.

**Diff**

```diff
+| Item | Conventional | Aerobic |
+|------|--------------|---------|
+| Install | $5k-$12k | $8k-$18k |
+| Electricity (20 yrs) | $0 | $4k-$7k |
+| Maintenance contract (20 yrs) | $0 | $6k-$10k |
+| Air pump replacement (20 yrs) | $0 | $600-$1,200 |
+| Pump-outs (20 yrs) | $1.5k-$3k | $1.5k-$3k |
+| **Total 20-yr** | **$6.5k-$15k** | **$20k-$39k** |
```

**Numbers verified against**

- Out West Septic field experience in Palo Pinto, Hood, Erath, Stephens, Young, Jack, and Eastland counties
- Texas A&M AgriLife Extension guidance on aerobic maintenance contract costs
- Current electricity rates in rural North Texas (about $0.12/kWh average)

---

*Out West Septic, TCEQ OSSF Installer I, OS0041298*