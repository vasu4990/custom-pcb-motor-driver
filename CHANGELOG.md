# Changelog

## Unreleased — engineering reference upgrade

### Added

- concrete TI DRV8848 reference profile with source provenance
- tolerance-aware current-limit, loss, thermal and derating calculations
- engineering design checker and generated report
- traceable BOM linter
- schematic connectivity-contract linter
- evidence-based release stage gate
- interface and test-point definitions
- EDA-independent CAD connectivity contract
- expanded electrical, thermal, PCB, validation, FMEA and manufacturing documentation
- comprehensive unit-test coverage and CI checks

### Changed

- replaced the IC-agnostic/TBD design core with an auditable DRV8848 reference implementation
- set the reference current-regulation network to 0.56 Ω / 1 W / 1% per bridge
- upgraded the README, design specification, architecture, bring-up, safety and contribution guidance

### Intentionally not claimed

- no fabricated PCB
- no completed real CAD/ERC/DRC evidence
- no measured hardware current, thermal, transient or EMI performance
