# First-Article Bring-Up

> Use a current-limited bench supply and keep motors mechanically safe. Do not begin with a battery capable of high fault current.

## 1. Unpowered inspection

- verify U1 pin-1 orientation and exposed-pad solder quality
- inspect all connectors and polarized parts
- verify no solder bridge at PWP pins
- measure VM-to-GND resistance
- measure each sense resistor
- verify nFAULT pull-up and VREF/VINT connection

## 2. Current-limited power-up, no motors

1. Set supply to the minimum intended VM and a low current limit.
2. Keep nSLEEP low.
3. Apply power.
4. Check supply current for abnormal draw.
5. Measure VINT.
6. Confirm nFAULT is not asserted.
7. Toggle nSLEEP and re-check fault/current.

## 3. Logic verification

With motors disconnected, exercise the control inputs and confirm startup/reset behavior never produces an unintended enabled state.

## 4. One-motor test

- connect only motor A
- start at low PWM duty
- observe VM, AISEN, AOUT1/AOUT2 and nFAULT
- increase duty gradually
- verify the configured current-chopping threshold
- stop and inspect temperature

Repeat for bridge B.

## 5. Dual-channel and thermal test

Run both channels at representative load, then toward the intended maximum operating point. Record VM, current, ambient, duration, package/board temperatures, fault events and current-limit behavior.

## 6. Release evidence

Put measured results in a dated validation record. Only then flip the corresponding booleans in `hardware/design_values.yaml`.
