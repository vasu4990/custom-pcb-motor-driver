# ADR-0001: Use DRV8848 as the concrete reference driver

- Status: Accepted for reference design
- Date: 2026-08-18

## Context

The repository originally left the H-bridge IC as `TBD`, which made current, thermal, decoupling, interface and layout guidance too abstract to verify.

## Decision

Use Texas Instruments DRV8848 in the PWP/HTSSOP package as the **concrete reference profile**, while keeping the higher-level design process reusable for another driver later.

## Reasons

- operating-voltage range covers the 6–12.6 V robot target
- two H-bridges in one device
- integrated current regulation through VREF/xISEN
- nFAULT output and nSLEEP control
- exposed thermal pad and documented layout guidance
- internal UVLO/OCP/thermal protection as secondary fault mechanisms

## Consequences

The repository can now have specific current-sense values, decoupling, thermal calculations, interface requirements and PCB rules. A future driver replacement must add a new reference profile and re-run/review every dependent calculation instead of silently editing prose.
