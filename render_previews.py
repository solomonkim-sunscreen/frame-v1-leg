"""Render preview images of the Frame v1 leg assemblies from STEP files.

Uses build123d to tessellate the STEP geometry and matplotlib 3D to render
a clean hero-style image with a transparent background.

Requires: pip install build123d matplotlib
Run from the repository root: python render_previews.py
"""
import os
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from build123d import import_step

ROOT = Path(__file__).resolve().parent
CAD = ROOT / "cad"
OUT = ROOT / "assets"


def render(step_path, out_path, elev=18, azim=-55, tol=1.0, color=(0.32, 0.44, 0.58)):
    part = import_step(step_path)
    verts, tris = part.tessellate(tol)
    verts = np.array([(v.X, v.Y, v.Z) for v in verts], dtype=float)
    tris = np.array(tris, dtype=int)
    print(f"{step_path}: {len(tris)} triangles, bbox min {verts.min(axis=0)}, max {verts.max(axis=0)}")
    mesh = verts[tris]  # (n_tri, 3, 3)
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111, projection="3d")
    coll = Poly3DCollection(mesh, alpha=1.0)
    coll.set_facecolor(color)
    coll.set_edgecolor((0.15, 0.19, 0.24))
    coll.set_linewidth(0.05)
    ax.add_collection3d(coll)
    mins = verts.min(axis=0)
    maxs = verts.max(axis=0)
    center = (mins + maxs) / 2.0
    size = (maxs - mins).max()
    ax.set_xlim(center[0] - size / 2, center[0] + size / 2)
    ax.set_ylim(center[1] - size / 2, center[1] + size / 2)
    ax.set_zlim(center[2] - size / 2, center[2] + size / 2)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    plt.tight_layout(pad=0)
    plt.savefig(out_path, dpi=160, transparent=True)
    plt.close(fig)
    print("saved", out_path)


if __name__ == "__main__":
    import os
    os.makedirs(OUT, exist_ok=True)
    render(f"{CAD}/Full_Legs.step", f"{OUT}/full-legs.png", elev=15, azim=-55, tol=1.0)
    render(f"{CAD}/Leg_1A.step", f"{OUT}/leg-1a.png", elev=15, azim=-55, tol=0.7)
    print("done")
