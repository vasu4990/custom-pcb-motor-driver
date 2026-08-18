# Architecture

```mermaid
flowchart LR
  BAT[6-12.6 V source] --> PROT[Protection front end]
  PROT --> DC[Local + bulk decoupling]
  DC --> U1[DRV8848 dual H-bridge]
  MCU[MCU] -->|AIN1/AIN2/BIN1/BIN2| U1
  MCU -->|nSLEEP| U1
  U1 -->|nFAULT| MCU
  U1 --> MA[Motor A]
  U1 --> MB[Motor B]
  U1 --> RSA[0.56R sense A]
  U1 --> RSB[0.56R sense B]
  RSA --> GND[Power ground / exposed pad]
  RSB --> GND
```

## Layers of responsibility

**Source/protection:** connector, fuse, polarity protection, transient clamp and optional input bulk capacitor.

**Power stage:** DRV8848, local VM decoupling, VINT bypass, exposed pad/thermal copper, motor connectors and sense resistors.

**Control:** four bridge inputs, nSLEEP, nFAULT and VREF.

**Verification:** machine-readable netlist contract, test points, calculation scripts, BOM linter, release-state gate and documented first-article test sequence.

The design intentionally keeps source-specific protection separate from the core driver because a bench supply, 2S/3S battery and long robot harness can require materially different surge and fuse decisions.
