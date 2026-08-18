# ADR-0002: Set the reference chopping limit below 1 A/bridge

- Status: Accepted for reference design
- Date: 2026-08-18

## Context

The DRV8848 recommended operating table specifies up to 1 A RMS per bridge. A nominal design set exactly at 1 A can exceed that value once VREF and sense-resistor tolerances are included.

## Decision

Tie VREF to VINT and use a **0.56 Ω, 1 W, 1%** sense resistor on each bridge.

The nominal model gives about 0.893 A full-scale chopping current. Including the stored VINT range and 1% resistor tolerance, the repository model keeps the resulting range below 1 A.

## Consequences

- normal stall/high-load current is managed by the chopping regulator rather than relying on OCP
- the sense resistor has significant dissipation and must be treated as a critical component
- motor compatibility must be checked because available stall torque is intentionally current-limited
- the exact regulation level still requires first-article measurement
