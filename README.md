# Custom PCB Motor Driver

Engineering documentation and starter design package for a compact dual-channel DC motor driver PCB intended for small robotics projects.

> **Status:** design specification / PCB-development scaffold. This repository does **not** claim a fabricated or electrically validated PCB yet. Final component values, copper widths, thermal performance, and protection choices must be verified against the selected motor, battery, and H-bridge IC.

## Design target

A reusable two-motor driver board with:

- Two bidirectional brushed-DC motor channels
- Logic-level PWM + direction control from a microcontroller
- Separate motor and logic power domains with common ground
- Reverse-polarity and transient-protection provisions
- Bulk + local decoupling
- Test points for supply, logic rail, and motor outputs
- Clear connectors for battery, motors, and MCU signals

## Recommended architecture

```text
Battery input
   |
Protection + bulk capacitance
   |
Dual H-bridge IC ---- Motor A
   |                 Motor B
   |
MCU header: PWMA/PWMB + direction + STBY + GND
```

For a small robot, a TB6612FNG-class device is a practical starting point. If your motors have higher stall current, select a driver based on **stall current**, not free-running current.

## Repository layout

- `docs/DESIGN_SPEC.md` — electrical requirements and review checklist
- `hardware/BOM.csv` — starter bill of materials
- Future: KiCad schematic / PCB files, Gerbers, fabrication notes, measurements

## Before routing a PCB

1. Measure motor stall current at the intended battery voltage.
2. Select an H-bridge with adequate continuous and peak current margin.
3. Confirm input-voltage limits under charger and regenerative conditions.
4. Size copper for current and temperature rise.
5. Put ceramic decoupling directly at IC supply pins.
6. Keep high-current motor loops short and away from logic traces.
7. Provide a low-impedance ground return.
8. Verify thermal dissipation using the package and PCB copper area.

## Validation plan

When hardware exists, record:

- No-load current
- Stall / peak-current behavior
- H-bridge package temperature under representative load
- Supply ripple at motor start/reversal
- Logic noise / resets during switching
- PWM-frequency behavior
- Reverse-polarity and brownout behavior

Adding oscilloscope captures and thermal images later will make this repository much stronger than simply uploading Gerbers.
