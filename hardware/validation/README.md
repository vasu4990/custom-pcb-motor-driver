# Hardware Validation Records

This directory is reserved for **measured first-article evidence**. Do not place simulation outputs or estimates here as if they were physical results.

For each physical board revision, copy `VALIDATION_RECORD_TEMPLATE.md` to a dated file such as:

```text
2026-09-14_rev-a_first-article.md
2026-09-15_rev-a_dual-channel-thermal.md
```

Attach raw data, oscilloscope screenshots or photos in a sibling directory if useful, and identify the board revision/commit SHA, supply, source current limit, motor/load, instrumentation and ambient conditions.

Validation booleans in `hardware/design_values.yaml` should only be changed after a record here supports the claim.
