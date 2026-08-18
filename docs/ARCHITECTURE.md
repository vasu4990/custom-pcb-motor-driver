# Electrical Architecture

## Functional blocks

1. **Power input** — battery or DC supply enters through a keyed/polarized connector.
2. **Protection** — optional fuse/PTC, reverse-polarity protection, and transient suppression appropriate to the application.
3. **Energy storage** — bulk capacitance near VM plus high-frequency ceramic decoupling at the driver.
4. **Motor driver** — dual H-bridge IC with PWM/direction inputs and any available standby/fault outputs.
5. **Logic interface** — clearly labeled MCU pins with a shared ground and voltage compatibility confirmed from the datasheet.
6. **Outputs** — two motor connectors with unambiguous channel/polarity labels.

## Grounding and current paths

High-current motor return paths should be short and wide and should not force switching current through sensitive logic-ground paths. Keep decoupling loops compact and follow the driver's recommended layout, especially for exposed thermal pads.

## Design philosophy

This repository separates **requirements** from **implementation**. Until exact CAD files and a chosen driver part are committed, the package is a reference design specification rather than a fabricated PCB release.
