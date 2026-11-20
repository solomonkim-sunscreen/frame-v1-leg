# Parts list

Derived from the STEP AP214 exports (`cad/Leg_1A.step`, `cad/Leg_1B.step`), exported from Onshape November 20, 2026. Leg 1A and Leg 1B are mirrors of each other and contain the same parts.

## Per leg

| Qty | Part | Notes |
|-----|------|-------|
| 2 | CubeMars AKE90-8 actuator assembly | Listed in the export as `AKE90-8...STEP` |
| 2 | McMaster-Carr 60645K121 | Ball joint rod end, 1/4"-28 thread, zinc-plated steel housing, chrome-plated steel ball |
| 11 | "Part 1" | The leg's own custom parts (thigh, calf/shank, ankle, foot, pins, links), exported without names |
| 7 | Other | Fasteners and links; see the STEP file for the full product list |

Totals per leg: 22 unique products, 21 solid bodies. In Onshape, each leg assembly shows 49 instances (including repeated parts).

## Full Legs assembly

`cad/Full_Legs.step` combines both legs into one assembly: 31 unique products, 27 solid bodies, 63 instances in Onshape. It contains the Leg 1A and Leg 1B subassemblies, plus the same AKE90-8 actuators and 60645K121 rod ends.

## Sourcing

- AKE90-8: CubeMars (AK series actuator)
- 60645K121: McMaster-Carr
