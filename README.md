# Frame v1 — Humanoid Leg

A humanoid robot leg assembly, designed at Sunscreen Inc. by Jaden Dodoo. Two mirrored legs (Leg 1A and Leg 1B) from the "Frame v1" Onshape document, released as open-source hardware.

## What's included

- `cad/Leg_1A.step` — Leg 1A assembly (STEP AP214)
- `cad/Leg_1B.step` — Leg 1B assembly (STEP AP214), the mirror of Leg 1A
- `cad/Full_Legs.step` — Full Legs assembly (STEP AP214), both legs combined
- `cad/Ball_Joint_Actuator.step` — Ball Joint Actuator, a 3-DOF ball joint gearbox (STEP AP214)
- `cad/Robotic_Elbow_Joint.step` — Robotic Elbow Joint, a belt-driven elbow (STEP AP214)

Each leg is a complete assembly: thigh, calf/shank, ankle, foot, pins and links, driven by CubeMars AKE90-8 actuators.

## Parts

Per leg, from the STEP export (22 unique parts, 21 solid bodies):

- 2 × CubeMars AKE90-8 actuator assemblies
- 2 × McMaster-Carr 60645K121 ball joint rod ends (1/4"-28 thread, zinc-plated steel housing, chrome-plated steel ball)
- 11 parts exported only as "Part 1" — the leg's own custom parts
- Remaining parts are fasteners and links (see `docs/parts.md`)

## Steven Beckley's designs

Two more designs by Steven Beckley, a former Sunscreen engineer, released under the same licence. Full write-ups and Onshape sources are in `docs/steven-beckley/`.

- **Ball Joint Actuator** — a 3-degree-of-freedom ball joint gearbox (yaw, pitch, roll). Roll is driven by angled miter gears; pitch by a larger 45° miter gear engaging teeth on the upper hemisphere; yaw by a third actuator (not yet integrated). Write-up: [`docs/steven-beckley/ball-joint-actuator.pdf`](docs/steven-beckley/ball-joint-actuator.pdf).
- **Robotic Elbow Joint** — a belt-driven elbow with a DAMIAO DM-J10010L-EC actuator near the shoulder, giving a 1:8 gear reduction. Theoretical peak torque 960 Nm (120 Nm × 8); ~100 kg lift at the actuator's 40 Nm running torque. Write-up: [`docs/steven-beckley/robotic-elbow-joint.pdf`](docs/steven-beckley/robotic-elbow-joint.pdf).

## How to open

Import the STEP files into FreeCAD, Onshape, Fusion 360, SolidWorks, or any CAD tool that reads STEP AP214. The files are standard STEP AP214, exported from Onshape.

## Origin

Designed by Jaden Dodoo at Sunscreen Inc. (sunscreen.energy). Source: the "Frame v1" document in Sunscreen's Onshape workspace (Sunscreen Inc > Legs > Frame), last modified October 5, 2026. Exported from Onshape November 20, 2026.

Steven Beckley's designs come from the same workspace: the "Ball Joint" document (Custom Actuators folder, last modified October 2, 2026) and the "Elbow" document (Arms folder, last modified October 1, 2026). Exported from Onshape November 20, 2026.

Note: the "Knee Motor Model" from the same folder is not in this release yet.

## License

Licensed under the CERN Open Hardware Licence Version 2 — Strongly Reciprocal (CERN-OHL-S-2.0). See `LICENSE`.

## Contributing

Issues and pull requests welcome.
