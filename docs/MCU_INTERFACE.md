# MCU Interface Contract

The motor-driver board should present a controller interface that is simple to integrate and safe during reset.

## Signals

| Signal | MCU direction | Purpose |
|---|---|---|
| AIN1 / AIN2 | output | bridge-A direction/PWM control |
| BIN1 / BIN2 | output | bridge-B direction/PWM control |
| nSLEEP | output | global driver enable / safe shutdown |
| nFAULT | input | open-drain fault indication |
| VREF | optional | current-limit reference; reference design ties this to VINT |
| VLOGIC | power input | only supplies the external nFAULT pull-up/header logic |
| GND | reference | common logic/power reference |

## Firmware safety contract

1. Configure motion-control outputs to their non-driving state before enabling the H-bridge.
2. Hold `nSLEEP` low through MCU reset and peripheral initialization.
3. Enable the driver only after the controller knows its intended motor commands.
4. Treat `nFAULT` assertion as a reason to disable motion and record diagnostic context.
5. Do not automatically re-enable indefinitely after repeated faults; require bounded retry or operator/system recovery policy.
6. On brownout/watchdog reset, return to `nSLEEP` disabled before restoring commands.

## PWM

The reference application targets 20 kHz PWM. This is below the semiconductor input-frequency limit and above typical audible range, but final switching behavior, motor acoustics, heating and EMI must be validated with the actual assembly.

The board-level interface does not assign MCU GPIO numbers; those belong to the consuming robot/controller project.
