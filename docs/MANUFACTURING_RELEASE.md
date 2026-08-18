# Manufacturing Release Package

A fabrication release should be immutable and tagged. It should contain at minimum:

- source schematic and PCB files
- schematic PDF
- board fabrication outputs (Gerbers or IPC-2581 as agreed with fabricator)
- NC drill files
- board outline and stack-up notes
- fabrication drawing
- assembly drawing
- BOM with manufacturer part numbers
- pick-and-place/centroid file for SMT assembly
- stencil/paste-layer review
- design-rule report
- ERC/DRC results or documented waivers
- SHA-256 hashes for the released manufacturing archive
- release notes with board revision and known limitations

Before ordering, perform a visual CAM review: board outline, plated/non-plated holes, copper-to-edge, solder mask, paste apertures, silkscreen polarity, pin-1 marks, connector orientation and exposed-pad geometry.

This repository intentionally blocks `fab-ready` status until real CAD outputs exist and are reviewed.
