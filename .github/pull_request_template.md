## Summary

Describe the electrical, CAD, tooling or documentation change.

## Evidence

- [ ] `pytest -q`
- [ ] `python tools/design_check.py`
- [ ] `python tools/bom_lint.py`
- [ ] `python tools/netlist_lint.py`
- [ ] `python tools/release_gate.py reference`

## Hardware-impact checklist

- [ ] Datasheet/source revision recorded for changed semiconductor facts
- [ ] BOM/design YAML updated if assumptions changed
- [ ] No unmeasured result is presented as hardware validation
- [ ] CAD/ERC/DRC claims include actual evidence (if applicable)
- [ ] Physical-test claims include board revision, supply, load and test conditions (if applicable)

## Risk

What can fail electrically, thermally, mechanically or during manufacturing because of this change?
