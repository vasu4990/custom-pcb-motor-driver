# DRV8848 Reference Profile

The repository's concrete reference implementation targets **Texas Instruments DRV8848** in the 16-pin PWP/HTSSOP package. The generic architecture is still reusable with other drivers; this profile exists so the electrical math and review process are auditable instead of leaving the key IC as `TBD`.

## Datasheet facts used by this repository

Source: TI DRV8848 datasheet, Rev. B (SLLSEL7B, revised April 2024).

| Parameter | Datasheet value used |
|---|---:|
| VM recommended operating range | 4–18 V |
| VM absolute maximum | 20 V |
| Motor RMS current per H-bridge | 1 A |
| Typical OCP trip | 2 A |
| PWM input range | up to 250 kHz |
| HS + LS RDS(on), 25 °C | 0.9 Ω typ |
| HS + LS RDS(on), 85 °C | 1.08 Ω typ |
| θJA, PWP | 40.3 °C/W |
| VINT | 3.13–3.47 V, 3.3 V typ |
| Current-sense gain relation | `IFS = VREF / (6.6 × RISENSE)` |
| VM local bypass | 10 µF minimum + 0.1 µF ceramic |
| VINT bypass | 2.2 µF, >=6.3 V |
| nFAULT | open-drain, external pull-up >1 kΩ |

Official references:

- https://www.ti.com/product/DRV8848
- https://www.ti.com/lit/gpn/DRV8848

## Why 0.56 Ω sense resistors

If VREF is tied to VINT, a nominal 0.56 Ω sense resistor gives:

```text
IFS = 3.3 / (6.6 × 0.56) ≈ 0.893 A
```

Using the datasheet VINT range and a 1% resistor, the repository's automated model estimates approximately **0.838–0.948 A** full-scale current. This deliberately keeps the worst-case modeled limit below the 1 A RMS-per-bridge recommended operating value.

At the nominal 0.893 A limit, each 0.56 Ω sense resistor dissipates about 0.447 W, so the reference BOM calls for a 1 W part and leaves additional package/pulse validation to CAD release.

## Important distinction

The DRV8848 OCP mechanism is a fault-protection function, not the normal motor current controller. The design uses the xISEN/VREF chopping regulator as the normal current limit and treats OCP as a secondary protection layer.
