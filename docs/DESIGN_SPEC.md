# Electrical Design Specification

## Intended use

Dual brushed-DC motor control for small educational/mobile robots. Exact ratings remain TBD until the target motor and battery are measured.

## Interfaces

### Power
- `VM`: motor supply input
- `VLOGIC`: logic supply if required by selected H-bridge
- `GND`: common logic and motor return

### Control
- `PWMA`, `AIN1`, `AIN2`
- `PWMB`, `BIN1`, `BIN2`
- `STBY/EN` where supported

### Outputs
- `A01`, `A02` → Motor A
- `B01`, `B02` → Motor B

## Protection targets

- Reverse-polarity protection at battery input
- Bulk electrolytic capacitor close to driver power entry
- 100 nF local ceramic decoupling at IC supply pins
- Optional TVS footprint selected for actual battery voltage
- Optional fuse / resettable fuse footprint
- Flyback handling according to the chosen H-bridge datasheet

## PCB layout rules

1. Keep the motor-current loop compact.
2. Use wide copper pours/traces for `VM`, motor outputs, and power ground.
3. Do not route sensitive logic traces through high-current switching loops.
4. Place decoupling components before routing signal traces.
5. Use thermal vias/large copper where the driver package exposes a thermal pad.
6. Place connectors at board edges and label polarity visibly.
7. Add test points for `VM`, logic rail, `GND`, and both motor channels.

## Required calculations before fabrication

- Motor stall current at min/max battery voltage
- Driver conduction loss estimate
- PCB trace/copper temperature-rise estimate
- Bulk-capacitance sizing for allowable supply droop
- TVS working/standoff voltage selection if used
- Connector and fuse current ratings

## Bring-up sequence

1. Inspect for shorts and polarity errors without power.
2. Power from a current-limited bench supply with motors disconnected.
3. Verify logic and motor rails.
4. Exercise one bridge output at low current.
5. Attach one unloaded motor.
6. Test both directions and PWM.
7. Repeat for second channel.
8. Increase load gradually while monitoring current and temperature.

## Evidence to add after hardware testing

- Schematic PDF
- PCB screenshots / renders
- Gerbers and fabrication revision
- Scope traces during start/reversal
- Thermal measurements
- Final verified BOM
- Known limitations and maximum tested operating point
