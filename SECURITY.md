# Security and Physical Safety

This project switches motor current and may be connected to batteries or other low-impedance sources. A design, firmware, wiring or assembly defect can create unexpected motion, overheating, high fault current or component failure.

## Safety baseline

- use a current-limited bench supply for first power-up
- keep a physical power disconnect accessible
- do not begin validation with a high-energy battery source
- verify polarity and VM-to-GND resistance before power
- keep the mechanism mechanically restrained during initial motor tests
- use appropriately rated probes and short oscilloscope ground connections around switching nodes
- allow components to cool between thermal/fault experiments
- do not intentionally short outputs unless the lab setup safely limits source energy

The repository is **not a safety-certified motor controller**. Internal OCP and thermal shutdown are secondary protection mechanisms, not substitutes for correct source protection, PCB thermal design, current regulation and system-level safety.

For a security issue involving repository automation or exposed credentials, report it without publishing secrets. For hardware-safety concerns, open an issue with the affected design revision and the conditions that produce the risk.
