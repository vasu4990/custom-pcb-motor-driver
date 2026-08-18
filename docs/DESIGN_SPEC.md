# Design Specification

## Mission

A compact two-channel brushed-DC motor-driver board for small mobile robots, with explicit current limiting, fault reporting, safe enable behavior, testability, and an engineering release process.

## Concrete reference implementation

| Requirement | Reference target |
|---|---|
| Driver | TI DRV8848PWPR |
| VM application range | 6–12.6 V |
| Driver operating range | 4–18 V |
| Channels | 2 brushed-DC motors |
| Expected running current | 0.75 A/channel |
| Nominal chopping limit | ~0.893 A/channel |
| Worst-case modeled chopping limit | <0.95 A/channel |
| PWM target | 20 kHz |
| Logic | 3.3 V MCU compatible |
| Current sense | 0.56 Ω, 1 W, 1% per bridge |
| Fault | nFAULT to MCU + test point |
| Safe enable | nSLEEP held disabled through controller startup |
| PCB reference | 2 layers, 2 oz copper, ground plane, exposed-pad thermal vias |

## Non-negotiable constraints

- never exceed the semiconductor recommended operating range in normal use
- use current regulation for the normal stall/current limit; OCP is secondary fault protection
- keep local VM bypass close to the driver
- solder the exposed pad to ground copper
- expose nFAULT and xISEN for validation
- do not mark the project `fab-ready` without real CAD/ERC/DRC evidence
- do not mark it `hardware-validated` without measured load/thermal data

## Machine-readable sources of truth

- `hardware/design_values.yaml` — application/design decisions
- `hardware/reference_profiles/drv8848.yaml` — semiconductor profile from the TI datasheet
- `hardware/cad/netlist_spec.yaml` — connectivity contract
- `hardware/BOM.csv` — selection/traceability state
