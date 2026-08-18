# Design Review Checklist

## Semiconductor and schematic

- [ ] DRV8848 current lifecycle/status re-checked before order
- [ ] PWP pin numbers checked directly against the datasheet
- [ ] PowerPAD connected to ground
- [ ] VM 0.1 µF and >=10 µF local ceramics present
- [ ] VINT 2.2 µF bypass present
- [ ] nFAULT external pull-up present
- [ ] 0.56 Ω current-sense networks match the intended current limit
- [ ] nSLEEP safe-start behavior defined
- [ ] every connector pin named and polarity marked

## Protection

- [ ] actual battery/source defined
- [ ] measured or datasheet motor stall current recorded
- [ ] fuse strategy coordinated with source/harness
- [ ] reverse-polarity strategy selected
- [ ] TVS/clamp selected from real transient requirement
- [ ] bulk capacitance justified from real wiring/source behavior

## PCB

- [ ] VM bypass loop is physically compact
- [ ] current-sense resistors are close to xISEN pins
- [ ] xISEN returns avoid motor-current ground drops
- [ ] outputs are short/wide and direct to connectors
- [ ] exposed-pad copper/vias reviewed
- [ ] ground plane continuity reviewed
- [ ] test points accessible
- [ ] copper width/vias reviewed against real stack-up/current/temperature rise

## CAD/manufacturing

- [ ] symbol and footprint independently checked
- [ ] ERC passed or waivers documented
- [ ] DRC passed or waivers documented
- [ ] board outline/mounting verified
- [ ] Gerber/drill CAM review complete
- [ ] BOM MPNs complete for every selected critical part
- [ ] assembly polarity/pin-1 marks verified

## Validation

- [ ] unpowered inspection passed
- [ ] current-limited no-load power-up passed
- [ ] nFAULT and nSLEEP verified
- [ ] bridge A motor test passed
- [ ] bridge B motor test passed
- [ ] dual-channel thermal test passed
- [ ] stall/current-limit test documented
