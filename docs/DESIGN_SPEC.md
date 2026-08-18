# Design Specification

## Purpose

Compact dual brushed-DC motor driver for educational/mobile robotics prototypes.

## Reference requirements

| Requirement | Target |
|---|---|
| VM nominal range | 6–12 V |
| Motor channels | 2 |
| Control | PWM + direction |
| Logic | 3.3 V / 5 V where driver supports it |
| Continuous current | determined by selected IC + PCB thermal design |
| Peak/stall current | must be below driver, connector, and copper limits |
| Fault handling | expose fault/standby pins when available |

## Required design decisions before CAD release

- Exact driver IC and package
- Motor connector type/current rating
- Input connector type/current rating
- Reverse-polarity strategy
- TVS/fuse/PTC strategy
- Bulk capacitance value and voltage rating
- Copper thickness and trace/via current calculations
- Thermal pad/via layout
- Mounting-hole size and board outline

## Interface naming

Recommended control header:

```text
GND
VLOGIC (only if required by selected driver)
AIN1
AIN2
PWMA
BIN1
BIN2
PWMB
STBY
FAULT (if available)
```

Pin names should match the chosen IC or be mapped clearly in the schematic.

## Acceptance criteria for a future hardware release

A release may be marked `hardware-validated` only after: ERC/DRC passes, assembly inspection, current-limited first power-up, logic tests, motor tests, stall/peak-current review, and a documented thermal/load test.
