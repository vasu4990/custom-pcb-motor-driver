# Board Bring-up Procedure

Use this only after a real PCB design has been fabricated and assembled.

## 1. Unpowered inspection

- Check component orientation and solder bridges.
- Verify input polarity markings.
- Measure resistance between VM and GND; investigate unexpectedly low resistance.
- Confirm no short between logic supply and ground.

## 2. Current-limited power-up

Power the board without motors using a bench supply with a conservative current limit. Verify expected logic/driver supply rails and ensure the board does not heat unexpectedly.

## 3. Logic test

With motors disconnected, toggle standby/direction/PWM inputs and verify the driver's output behavior with appropriate measurement equipment.

## 4. Low-duty motor test

Connect one motor and command a low PWM duty cycle. Verify direction, current draw, and fault behavior. Repeat for the second channel.

## 5. Load and thermal validation

Increase load gradually while monitoring current and temperature. Compare measured behavior with driver datasheet limits and the PCB thermal assumptions.

## Record results

Document supply voltage, motor model, no-load current, loaded current, peak current, ambient temperature, hottest measured component, test duration, and any fault events.
