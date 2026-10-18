# Out West Septic manual quote worksheet

Copy this blank template into a private project record. The headings and field names are an input specification for a possible future `OutWestSepticQuoteBuilder`; no such executable class, workbook or macro is supplied here.

The associated project is [Out West Septic](https://outwestseptic.com). Leave contact details, credentials and signatory blank until the business confirms what belongs on the specific quote. A completed worksheet is not automatically an accepted contract or permission to construct.

## 1. Quote identity and scope

| Field | Value to supply | Evidence / checked by / date |
|---|---|---|
| Quote ID and revision | | |
| Preparation date | | |
| Customer / private project reference | | |
| Project location and applicable authority | | |
| Proposed work and system components included | | |
| Plans, evaluation or specification version used | | |
| Scope exclusions and work by others | | |
| Unknown conditions and required follow-up | | |
| Valid-through date, if approved | | |
| Prepared by / approved business contact | | |

Choose a unique identifier; a worksheet row number or changing `TODAY()` value is not a stable quote identifier or issue date. A later scope or price change needs a new revision and a record of what changed.

## 2. Itemized inputs

Repeat rows as needed. No line item implies that a particular service, fee, component or method is required.

| ID | Description / included scope | Quantity | Unit | Unit price (USD) | Line amount (USD) | Status: included / allowance / optional | Dated source or estimate basis |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

Possible categories to consider are materials, labor, equipment, site preparation, restoration and authority fees. Use the actual scope to decide which apply. Record the source and payer of an authority fee; do not add both a bundled fee and a duplicate separate charge.

For a priced line, manually calculate quantity multiplied by unit price and record the amount. Use consistent units, nonnegative finite inputs and an agreed currency-rounding method. A missing price is unresolved, not a zero-dollar inclusion. Keep optional work outside the included total unless the quote expressly includes it. Explain every allowance and its reconciliation method.

## 3. Adjustments, tax review and totals

| Item | Amount (USD) | Basis / source / reviewer |
|---|---|---|
| Included line-item subtotal | | |
| Authorized additions not already included | | |
| Authorized discounts or credits | | |
| Pre-tax quoted amount | | |
| Tax amount to charge customer, if applicable | | |
| Total quoted amount | | |
| Amount due at acceptance, if approved | | |
| Remaining payment schedule | | |

Reconcile the pre-tax amount as subtotal plus additions minus credits, then add only the reviewed customer tax amount. Deposits are payments against the quoted total, not extra work charges. Identify any amount shown separately but already included in the total.

**Do not apply a blanket 8.25% tax to the subtotal.** The [Texas Comptroller's real-property repair/remodeling guidance](https://comptroller.texas.gov/taxes/publications/94-116.php) distinguishes property use and contract structures; this worksheet does not classify a particular project. Record the classification, taxable base, applicable rate or exemption, source/date and tax reviewer's determination in the private project record. Do not treat an unknown tax amount as zero or issue a final total until the tax treatment is resolved.

## 4. Business terms supplied by the owner

| Topic | Approved wording / value | Approved by / date / reference |
|---|---|---|
| Payment milestones and methods | | |
| Changes to scope and authorization process | | |
| Unforeseen site conditions / allowance reconciliation | | |
| Permit and other work responsibilities | | |
| Proposed scheduling and dependencies | | |
| Warranty, exclusions and component documentation | | |
| Quote acceptance process and authorized signatory | | |

No deposit percentage, validity period, financing, warranty or response time is supplied by this template. Do not infer these terms from another project or publish an unapproved promise.

## 5. Release review

- [ ] Scope, exclusions, quantities and units match the referenced proposal/plans.
- [ ] Every included amount has a source or clearly labeled estimate basis.
- [ ] Optional items, allowances, fees and credits are reconciled without duplication.
- [ ] Tax treatment and final total are reviewed; no unknown amount became zero.
- [ ] Business terms, contact details and signatory are confirmed for this quote.
- [ ] Revision, approval date and delivery record are retained privately.

| Release record | Value |
|---|---|
| Reviewer and date | |
| Outstanding conditions | |
| Status: working draft / approved for issue / superseded | |
| Approved revision | |
| Delivery date and intended recipient | |

## Evidence and implementation status

The tables are repository workflow recommendations, not a published tax or contract form. The Comptroller source was accessed 2026-10-18; applicability to an actual project still requires review. [Open decisions](outwestseptic_quote_builder_decisions.md) identify what is needed before automation. No PDF export, emailing, workbook calculation or professional review has been completed by this template.
