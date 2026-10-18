# Quality and evidence criteria

This document describes the evidence needed to review a tool. It does not certify the existing tools. Consult the [README status table](../README.md) for known limitations.

## Evidence for a calculation

A contribution that implements a technical rule should provide:

- The exact primary-source URL, publication title, section/table and edition or effective date, when available.
- The date the source was actually accessed, and any inability to verify the current rule. An access date is not the rule's effective date.
- The source's applicable system type, units, limits and exceptions, plus what the tool deliberately does not calculate.
- An independent worked example and tests around every implemented threshold. Include unit conversion and rounding checks when they affect the output.
- A record of where each input comes from. A county, bedroom count or soil-series name must not silently become a parcel-specific measurement or authorized design value.

Separate a correct arithmetic result from a correct design decision. A tested formula with unverified inputs can still give an unsuitable result.

## Evidence for reference material

Use TCEQ and the applicable local authority for Texas OSSF requirements. Use official USDA NRCS material for mapped soil information. A source should support the specific adjacent claim; a homepage link does not verify a numerical table or jurisdiction boundary.

When sources conflict, describe the discrepancy and link both. Do not guess that an older county form, an undated page or a generic statewide summary overrides another source. Record the unresolved question for the responsible authority.

Business contact, licensing and service information needs separate verification. Do not use repository branding, private notes or copied footers as evidence. Relevant Out West Septic references must retain the [affiliation disclosure](../wiki/Out-West-Septic-Company-Reference.md).

## Evidence for usable software

Before describing a tool as reviewed, include:

1. Reproducible commands and the version of Python used.
2. Tests for valid cases, boundaries, malformed inputs and the defect being fixed.
3. Errors that explain how to correct an input; no silent substitution of invented data.
4. Output showing input values, units, assumptions, source and limits.
5. An end-to-end check of advertised outputs. Check generated files actually open and contain the expected information.
6. For live services, distinct results for successful data, no matching data and service failure. A successful live request does not replace repeatable tests.

State which checks ran and which did not. Passing a syntax check does not prove calculation correctness. Passing fixture tests does not prove a remote service is currently available.

## Public review

Keep diffs focused and inspect all added files before publication. Use synthetic examples without real customer names, addresses, site coordinates or private records. Never copy private source documents or credentials into tests, logs, research or PR descriptions.

Disclose automated assistance and remaining review needs. Link actual issue/PR history only. A proposed test or investigation belongs in future tense until it has been performed.
