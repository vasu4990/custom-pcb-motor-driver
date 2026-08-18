# CAD Handoff

This directory intentionally does **not** contain invented KiCad/Altium files. The current repository is an engineering-complete **reference design**, not a fabricated-board claim.

`netlist_spec.yaml` is the machine-readable connectivity contract that the first real CAD schematic must implement. When CAD is created, add:

```text
hardware/cad/<project>.kicad_pro
hardware/cad/<project>.kicad_sch
hardware/cad/<project>.kicad_pcb
```

(or the equivalent source format), then update `hardware/design_values.yaml` validation fields only after symbol/footprint review, ERC and DRC actually pass.

The release gate deliberately fails `cad-ready` and `fab-ready` today. That is a feature: the repository cannot silently turn placeholders into fake validation claims.
