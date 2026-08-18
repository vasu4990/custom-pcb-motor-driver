# Thermal Design and Power Budget

This document separates **screening math** from **hardware validation**.

## Conduction model

For one active bridge, the simple conduction estimate is:

```text
Pbridge ≈ Irms² × (RDS_HS + RDS_LS)
```

The DRV8848 profile uses 0.90 Ω typical total path resistance at 25 °C and 1.08 Ω typical at 85 °C.

At the reference 0.893 A nominal current limit:

- two bridges, 25 °C RDS(on) model: about **1.44 W** total conduction loss
- two bridges, 85 °C RDS(on) model: about **1.72 W** total conduction loss

At the expected 0.75 A/channel operating point, the 25 °C model is about **1.01 W** total.

## Junction screening

The automated checker uses the datasheet θJA value of 40.3 °C/W only as a screening metric. With the reference current limit and 25 °C ambient, the rough calculation is about 83 °C junction. A deliberately harsher screen uses the high-temperature RDS(on), worst-case current-limit tolerance, and 50 °C ambient; it remains below the 150 °C operating-junction ceiling in the simple model.

**This is not a board temperature prediction.** θJA depends strongly on PCB copper, airflow, board size, thermal-via implementation and measurement method.

## PCB thermal strategy

- exposed PowerPAD soldered to ground copper
- ground plane under/around the driver
- reference target of 9 thermal vias under the pad, 0.30 mm finished hole
- short, wide output/current-return paths
- 2 oz copper reference stack-up
- test point access for VM, xISEN and nFAULT

The via count, drill, copper and stencil aperture must be finalized with the actual PCB fabricator/assembler.

## Hardware validation requirement

A design cannot be marked `hardware-validated` until temperature rise is measured with both channels loaded, at the maximum intended supply, at realistic ambient, and with motor transients represented. Record ambient, board temperature, package-top temperature, current, duty cycle, VM, test duration and shutdown/fault behavior.
