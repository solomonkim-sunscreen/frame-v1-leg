# Steven Beckley's designs

Two designs by Steven Beckley (former Sunscreen engineer), written up in the
decks below. Both are released under the same
[CERN-OHL-S-2.0](../../LICENSE) licence as the Frame v1 leg.

## Ball Joint Actuator (Ball Joint Gearbox)

A 3-degree-of-freedom ball joint gearbox: **yaw, pitch and roll**.

- **Roll** is driven by a set of angled miter gears, transferring rotation
  from the base to the end effector in any position.
- **Pitch** is driven by a larger 45° miter gear engaging teeth inset on the
  upper hemisphere of the actuator. Pitch rotates at a 45° off-angle; the
  horizontal component can be offset by simultaneous yaw rotation.
- **Yaw** is to be driven by a third actuator rotating the entire orb about
  its axis. Not yet integrated. Two integration methods are proposed:
  1. Rotate the entire assembly (actuators included) about the base —
     simple but inefficient, since the bottom actuator moves more weight.
  2. Mount the actuators together and transfer rotation to the base of the
     gearbox through a gear system — more energy efficient, but technically
     complicated, and the upper actuators may need to rotate to offset the
     gearbox rotation.

**Current issues (as documented):**

- 3D-printed gears have more play and slip more than metal ones. The miter
  gears in the CAD were pulled from real metal gears (McMaster or Grainger)
  and should be easy to integrate, but the teeth on the upper hemisphere
  that enable pitch rotation are custom and would need a CNC mill.
- The housing and several shaft adapters are currently 3D printed; they are
  weak and may fail under heavy loads. Ideally most components would be
  aluminium or steel, but their complex geometries may present
  manufacturing problems.
- Pitch miter gear angle is an open issue.

Write-up: [ball-joint-actuator.pdf](ball-joint-actuator.pdf) ·
[Google Slides](https://docs.google.com/presentation/d/1_wKGdSW88S-50Kzz6g19qIi0tzMg8YD6YG7Vpj5AH5A/edit?usp=sharing)

## Robotic Elbow Joint

A belt-driven elbow joint with the actuator placed closer to the shoulder.

- Actuator: DAMIAO DM-J10010L-EC, located near the shoulder joint.
- The belt system reduces the moment the actuator's weight creates on the
  shoulder, and gives a simple gear reduction that increases torque output.
- **Gear reduction: 1:8.**
- **Belt tensioning:** the arm is split into two pieces that move axially to
  tension the belt, joined by two bolts. The gap cannot be changed while the
  belt is installed — it must be set beforehand — so this needs improvement.

**Testing (theoretical, as documented):**

- Peak torque: 960 Nm (120 Nm × 8). With a 0.32 m forearm that is 3,000 N
  of force, about 306 kg. Other components would likely fail before the
  motor at that load.
- At the actuator's running torque (40 Nm) the arm should lift ~100 kg.
- An angular velocity test should also be performed. The arm still needs a
  strength test with the actuator installed.

Write-up: [robotic-elbow-joint.pdf](robotic-elbow-joint.pdf) ·
[Google Slides](https://docs.google.com/presentation/d/1XkT5sVUbxmHS56uevfUegRm1PMH_rO07iDVszvKCdOo/edit?usp=sharing)

## CAD

The Onshape CAD for these designs is exported as STEP AP214 in
[`cad/`](../../cad/) alongside the leg files.

- **Ball Joint Actuator** — [`cad/Ball_Joint_Actuator.step`](../../cad/Ball_Joint_Actuator.step)
  (Assembly 1, 9 instances, 13 mates; Onshape document
  ["Ball Joint"](https://cad.onshape.com/documents/ddb2c615518c03c9c3dc84c7/w/61f57c0fb637e14f18eb9f83),
  folder "Custom Actuators", last modified Oct 2, 2026 by Steven Beckley).
- **Robotic Elbow Joint** — [`cad/Robotic_Elbow_Joint.step`](../../cad/Robotic_Elbow_Joint.step)
  (Part Studio 1, 77 features; Onshape document
  ["Elbow"](https://cad.onshape.com/documents/d3cde0dbefea28b14d9c2ec2/w/7d1bec9a9944b91df184ef64),
  folder "Arms", last modified Oct 1, 2026 by Steven Beckley). The document's
  Assembly 1 is empty, so Part Studio 1 is the design's top-level element.
