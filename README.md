# PYTHON_MANIM

This repository contains a collection of Python scripts for creating mathematical animations using [Manim](https://docs.manim.community/).

## Prerequisites

- **Python 3.8+** (recommended)
- **Manim**

You can install Manim globally or inside a virtual environment. For more details, see the [Manim installation guide](https://docs.manim.community/en/stable/installation.html).

## Setting Up the Project

1. **Create and activate a virtual environment:**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   *(On Windows PowerShell. For other shells, use the appropriate activation command.)*

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Verify Manim installation:**
   ```powershell
   manim --version
   ```

## Running Manim Scenes

To render a scene, use the following command:
```powershell
manim <script_name.py> <SceneClassName>
```
For example:
```powershell
manim CSC-01.py CosecantSquaredGraph
```

## Scene Inventory

| Scene Class | File | Math / Topic Summary |
| --- | --- | --- |
| `CosecantSquaredGraph` | `CSC-01.py` | Plots a cosecant-based trig graph with discontinuities and pi-labeled x-axis. |
| `SlopeField` | `DE-SlopeField.py` | Builds slope fields for first-order differential equations (`dy/dx = -x/y`, `x+y`, `y`). |
| `DotAlongCurve` | `DotAlongCurve.py` | Tracks a point on a quadratic curve and moves it to the parabola's minimum. |
| `EpsilonDeltaLimitScene` | `EpsilonDeltaLimitProof_01.py` | Visualizes epsilon-delta limit neighborhoods around `x=C` and `y=L` on a function graph. |
| `CircleEquation` | `Manim-Circle.py` | Draws the implicit circle `x^2 + y^2 = 1` on coordinate axes. |
| `SigmoidFunction` | `Manim-Sigmoid01.py` | Plots the logistic sigmoid with configurable weight and bias parameters. |
| `SineWave` | `Manim-Sine.py` | Graphs `sin(x)` over `[-pi, pi]` with key pi-based angle labels. |
| `UnitCircle` | `Manim-UnitCircle.py` | Animates radius rotation on a unit circle with angle `theta` annotation. |
| `DiscontinuityScene01` | `Python-Discontinuity.py` | Shows a removable discontinuity (hole) in a rational function graph. |
| `PolarCircle` | `Python-PolarCircle.py` | Uses polar coordinates to animate a point on a circle with tangent behavior. |
| `RiemannSumApproximation` | `RSum01.py` | Approximates area under `y=x^2` using left Riemann rectangles with decreasing `dx`. |
| `SineWave` | `SIN-01.py` | Basic sine curve plot over `[-pi, pi]`. |
| `SigmoidFunction` | `Sigmoid.py` | Logistic sigmoid plot with displayed weight and bias values. |
| `CustomTangentGraph` | `TAN-01.py` | Tangent-function style graph with asymptote-safe clipping behavior. |
| `TangentAnimation` | `TangentLine01.py` | Animates motion along the cubic function `f(x)=x^3` (tangent-focused setup). |
| `TangentLineExample` | `Tangent_01.py` | Draws a parabola with a tangent line at a selected point. |
| `TaylorPoly` | `TaylorPoly-ln(x).py` | Compares `ln(x)` with increasing-degree Taylor polynomial approximations around `C=2`. |
| `FixedInFrameMObjectTest` | `ThreeDimensional01.py` | 3D axes scene demonstrating fixed-in-frame text overlay. |
| `ThreeDLightSourcePosition` | `ThreeDimensional02.py` | 3D parametric surface scene with adjusted light-source position. |
| `ThreeDSurfacePlot` | `ThreeDimensional03.py` | Plots a Gaussian-like 3D surface over the `(x,y)` plane. |
| `CircleWithRotatingRadius` | `UnitCircle.py` | Rotates a radius line around a circle to illustrate full-angle sweep. |
| `CircleWithTriangle` | `UnitCircle02.py` | Animates radius rotation with dynamic sine/cosine triangle projections. |
| `SquareToCircle` | `manim01.py` | Demonstrates geometric transformation from square to circle. |
| `Updaters` | `manim01.py` | Shows updater-driven motion of a `ln(2)` math label and surrounding box. |
| `Scaling` | `manim01.py` | Demonstrates geometric scaling and repositioning of basic shapes. |
| `RiemannSumScene` | `riemann_sum.py` | Shows Riemann-sum convergence for `y=x^2` alongside exact integral area/error. |

## Testing

The `tests/test_scenes.py` script renders every Manim scene in the project and reports whether each one built successfully.

**Run it** (with the venv active):
```bash
python tests/test_scenes.py
```

**Options:**
| Flag | Default | Description |
| --- | --- | --- |
| `--quality l\|m\|h` | `l` | Render quality: low / medium / high |
| `--log <path>` | `tests/test_scenes.log` | Path for the log file |

The script scans all `.py` files in the project root, detects classes that inherit from a Manim scene base (e.g. `Scene`, `ThreeDScene`), and runs `manim` on each one. Results are printed to the terminal and written to the log file with full error output for any failures.

---

## Recommended VS Code Extension

For a better development experience, install the **Manim Sideview** extension in VS Code. It provides live preview and integration for Manim projects.

- [Manim Sideview Extension](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview)

## Additional Notes

- Output videos and images are saved in the `media/` folder by default.
- For LaTeX rendering, ensure you have a working LaTeX distribution installed (e.g., MiKTeX or TeX Live).

---

For more information, see the [Manim documentation](https://docs.manim.community/).
