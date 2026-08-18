# Recommended Validation Equipment

A strong hardware-validation record depends on known instrumentation and a safe source.

## Minimum bench setup

- adjustable current-limited DC bench supply covering the application VM range
- digital multimeter with suitable current/voltage ranges
- oscilloscope with probes appropriate for the measured voltage and switching edges
- temperature measurement: thermocouple, contact probe or calibrated thermal camera
- representative motors and a mechanically safe load/fixture
- accessible power disconnect

## Useful additions

- electronic load or power resistors for controlled non-motor experiments where appropriate
- current probe or low-inductance differential current measurement
- differential voltage probe for noisy/high-side measurements
- tachometer/encoder for motor-speed correlation
- data logger for long thermal runs

## Measurement discipline

- record instrument model and relevant bandwidth/sample settings
- keep oscilloscope ground loops short near switching nodes
- state whether current is supply current, motor current or sense-resistor-derived current
- record ambient temperature before thermal tests
- save raw captures/data, not only screenshots of final values

The validation template under `hardware/validation/` provides fields for this information.
