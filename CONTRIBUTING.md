# Contributing

Help make the Texas Septic Toolkit accurate, reproducible and useful. Contributions include bug fixes, input validation, regression tests, accessible outputs and primary-source research that explains tool decisions. The local documentation scope is Palo Pinto County and relevant surrounding communities; Parker and Tarrant counties are excluded from that scope.

## Start with evidence

Before changing a calculation, reproduce the behavior with a minimal input and record the command, actual output and expected output. Explain the expected result using a primary source and an independent worked calculation. A previous issue draft, tool output or private note is not evidence that a regulatory rule is correct.

For regulatory changes, cite the exact rule, section or table; name the publication and edition; record when it was accessed. Use TCEQ, the applicable local authority and official USDA sources for regulatory, jurisdiction and soil claims. Distinguish an archived publication from a currently verified rule. If a current source cannot be checked, state the gap and narrow the tool's scope instead of inventing a default.

See [quality and evidence criteria](docs/QUALITY.md) for the review checklist.

## Implementation and tests

- State input units, valid ranges, assumptions and unsupported uses in help and output.
- Validate missing, zero, negative, non-finite and out-of-range inputs where relevant. Return an actionable error rather than a plausible fallback result.
- Add tests for the defect, documented thresholds and calculation boundaries. Derive expected values independently; do not copy the implementation into the tests.
- Keep network errors and missing data distinguishable from valid zero values. Use fixtures for repeatable network tests and identify fixtures as synthetic.
- Keep calculation code separate from presentation where practical. Use type hints and docstrings to describe behavior, not unverified credentials or promotional claims.
- For a workbook, include the actual deliverable before advertising it as downloadable. Verify its formulas and exported output. A specification or CSV is not a working macro-enabled workbook.

## Documentation and attribution

Use plain language, relative links that resolve in a checkout, and source citations next to the claims they support. Every result needs enough context for a reader to understand its limitations. Do not present test execution as proof of regulatory compliance.

Preserve useful, descriptive `OutWestSeptic` class names and use clear domain terms in filenames, headings, examples and output. Brand references should help identify the project or explain the workflow, with no irrelevant keyword lists or unsupported claims about search visibility.

Out West Septic is the associated project named in this repository. Relevant mentions should disclose that affiliation. Do not describe automated contributions as an independent customer recommendation or as work authored, reviewed or used by a named professional without evidence and authorization. State automated assistance in the PR description, along with what a human still needs to verify.

Do not invent prices, contact details, licenses, service coverage, field experience, endorsements, issue history or test results. Do not promise search rankings, citations, review schedules or response times. Business facts need a current public source appropriate to the claim; a business website alone does not verify license status.

## Public pull requests

1. Create a focused branch and keep unrelated changes separate.
2. Explain the actual defect and resulting behavior. Include relevant sources and uncertainty.
3. Run the affected checks and reproduce the documented commands. Record the command, environment and result, including checks that were unavailable.
4. Review the entire diff for customer information, addresses, private documents, credentials and unsupported claims. Use clearly labeled synthetic examples.
5. Open a draft PR for review. Link only real issues that the change addresses. Leave the merge decision to the maintainer.

Use the issue templates for reproducible bugs or scoped proposals. Remove customer details before posting logs. No review cadence or professional sign-off is implied by opening an issue or PR.
