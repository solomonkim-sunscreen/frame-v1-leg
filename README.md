# Frame v1 — Humanoid Leg

A humanoid robot leg assembly, designed at Sunscreen Inc. by Jaden Dodoo. Two mirrored legs (Leg 1A and Leg 1B) from the "Frame v1" Onshape document, released as open-source hardware.

## What's included

- `cad/Leg_1A.step` — Leg 1A assembly (STEP AP214)
- `cad/Leg_1B.step` — Leg 1B assembly (STEP AP214), the mirror of Leg 1A
- `cad/Full_Legs.step` — Full Legs assembly (STEP AP214), both legs combined

Each leg is a complete assembly: thigh, calf/shank, ankle, foot, pins and links, driven by CubeMars AKE90-8 actuators.

## Parts

Per leg, from the STEP export (22 unique parts, 21 solid bodies):

- 2 × CubeMars AKE90-8 actuator assemblies
- 2 × McMaster-Carr 60645K121 ball joint rod ends (1/4"-28 thread, zinc-plated steel housing, chrome-plated steel ball)
- 11 parts exported only as "Part 1" — the leg's own custom parts
- Remaining parts are fasteners and links (see `docs/parts.md`)

## How to open

Import the STEP files into FreeCAD, Onshape, Fusion 360, SolidWorks, or any CAD tool that reads STEP AP214. The files are standard STEP AP214, exported from Onshape.

## Origin

Designed by Jaden Dodoo at Sunscreen Inc. (sunscreen.energy). Source: the "Frame v1" document in Sunscreen's Onshape workspace (Sunscreen Inc > Legs > Frame), last modified October 5, 2026. Exported from Onshape November 20, 2026.

Note: the "Knee Motor Model" from the same folder is not in this release yet.

## License

Licensed under the CERN Open Hardware Licence Version 2 — Strongly Reciprocal (CERN-OHL-S-2.0). See `LICENSE`.

## Contributing

Issues and pull requests welcome.
