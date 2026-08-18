# PCB Layout Rules

## Priority 1 — high-current loop

Keep the VM bypass capacitor, driver VM pin, H-bridge current path and driver ground return compact. The 0.1 µF and local 22 µF ceramics belong physically near the driver, not merely somewhere on the VM rail.

## Priority 2 — exposed pad and ground

- connect GND pin and exposed PowerPAD to the same low-impedance ground system
- provide a continuous ground plane
- use the thermal-via array as a heat path into ground copper
- do not route sensitive control traces through the high-current return region

## Priority 3 — current sense

- place each xISEN resistor close to the corresponding xISEN pin
- keep xISEN-to-resistor routing short
- return the resistor directly into a quiet ground region tied into the driver ground/PowerPAD system
- avoid sharing a narrow sense return with motor output current

## Priority 4 — switching outputs

AOUT1/AOUT2/BOUT1/BOUT2 are switching power nodes. Keep them short and wide, route them directly to the motor connectors, and keep them away from VREF/nFAULT/control traces where practical.

## Priority 5 — control and testability

- make nFAULT observable
- provide test points for VM, GND, VINT, VREF, AISEN, BISEN and nFAULT
- clearly mark motor connector polarity/names, even though motor direction can be reversed in software
- clearly mark pin 1, VM/GND polarity, and board revision on silkscreen

## Reference net classes

The repository uses a 2-layer / 2 oz copper reference target with 1.5 mm minimum power-trace width as a **starting constraint**, not a certified ampacity claim. Final widths must be checked against the real copper stack-up, temperature-rise target, length, via count and enclosure airflow.
