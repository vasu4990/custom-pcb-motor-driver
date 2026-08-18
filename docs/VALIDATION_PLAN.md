# Validation Plan

## Stage 0 — reference design

Automated checks must pass:

- YAML/profile parse
- design math
- BOM lint
- connectivity-contract lint
- reference release gate

## Stage 1 — CAD ready

Required evidence:

- completed schematic
- verified DRV8848 symbol and PWP footprint against datasheet
- connector footprints checked against manufacturer drawings
- ERC clean or every waiver documented

## Stage 2 — fabrication ready

Required evidence:

- PCB layout completed
- DRC clean or every waiver documented
- Gerber/drill visual review
- exposed-pad/stencil review
- 3D/assembly review for connector orientation and mechanical access
- fabrication drawing and board stack-up recorded

## Stage 3 — first article

1. Inspect unpowered assembly.
2. Check VM-to-GND resistance for shorts.
3. Power from a current-limited bench supply with motors disconnected.
4. Verify VINT.
5. Verify nSLEEP behavior and nFAULT high state.
6. Exercise each logic input without a motor.
7. Connect one motor at low duty cycle.
8. Verify current-chopping threshold with xISEN measurement.
9. Repeat for bridge B.

## Stage 4 — load/thermal

- run each channel independently
- run both channels simultaneously
- test minimum, nominal and maximum application VM
- test representative load and current-limit operation
- observe nFAULT during acceleration/reversal
- record package/board temperature rise
- evaluate supply transients at VM with short probe loop

## Stage 5 — abuse/fault characterization

Only with safe current limiting and appropriate lab controls:

- commanded reversal under realistic inertia
- motor disconnect/reconnect behavior
- brownout/recovery
- current-limit dwell
- short-circuit behavior only if the test setup safely limits source energy

Never use OCP/thermal shutdown as normal operating modes.
