# Contributing

Contributions are welcome, but this repository treats **traceability and evidence** as part of the design.

## Engineering rules

1. Keep semiconductor facts tied to an official datasheet/product source and record the revision/date when adding a reference profile.
2. Put design assumptions in machine-readable files where practical (`hardware/design_values.yaml`, reference profiles, BOM or connectivity contract), not only in prose.
3. Do not replace application-specific protection components with guessed part numbers presented as finalized choices.
4. Keep calculation functions pure and unit-tested.
5. Run the engineering checks before submitting changes.
6. Never flip a validation boolean to `true` without the corresponding real evidence.
7. Do not claim measured performance from simulation or thermal screening math.

## Local checks

```bash
python -m pip install -r requirements-dev.txt
pytest -q
python tools/design_check.py
python tools/bom_lint.py
python tools/netlist_lint.py
python tools/generate_report.py
python tools/release_gate.py reference
```

If a contribution includes real CAD, also explain symbol/footprint verification, ERC/DRC status and manufacturing-output review. If it includes physical test results, record the board revision, supply, motor/load, instrumentation, ambient conditions and test method.
