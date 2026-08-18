# Design Review Checklist

## Schematic

- [ ] Exact driver part number selected
- [ ] Datasheet-recommended decoupling present
- [ ] Logic voltage compatibility verified
- [ ] Standby/fault defaults defined
- [ ] Reverse-polarity behavior reviewed
- [ ] Motor stall current compared with IC limits
- [ ] Capacitor voltage ratings checked

## PCB

- [ ] Motor-current traces sized for copper stack-up
- [ ] Driver thermal pad/vias follow datasheet guidance
- [ ] Decoupling capacitors placed close to supply pins
- [ ] High-current loops kept compact
- [ ] Logic routing kept away from noisy motor switching where practical
- [ ] Connectors clearly labeled
- [ ] Pin 1 / polarity markings visible
- [ ] Mounting holes and board outline verified
- [ ] ERC/DRC clean or waivers documented

## Release

- [ ] BOM matches schematic
- [ ] Footprints checked against manufacturer drawings
- [ ] Gerber preview inspected
- [ ] Fabrication notes specify stack-up/copper assumptions
- [ ] Hardware status remains unvalidated until bring-up is completed
