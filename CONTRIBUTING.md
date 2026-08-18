# Contributing

Contributions should improve traceability and engineering confidence.

- Cite the exact component/datasheet assumption behind electrical limits.
- Keep measured values separate from calculated or target values.
- Do not describe an unbuilt board as tested or production-ready.
- For BOM changes, update `hardware/design_values.yaml` when the design envelope changes.
- Run `pytest -q` before submitting utility changes.
- Hardware changes should include ERC/DRC evidence when real CAD files are added.
