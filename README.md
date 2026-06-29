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
manim Manim-CosecantGraph.py CosecantGraph
```

## Scene Inventory

| Scene Class | File | Math / Topic Summary |
| :--- | :--------------------------- | :--- |
| `SquareCircle` | `Manim-BasicShapes.py` | Demonstrates geometric transformation from square to circle. |
| `LabelUpdater` | `Manim-BasicShapes.py` | Shows updater-driven motion of a `ln(2)` math label and surrounding box. |
| `ShapeScaling` | `Manim-BasicShapes.py` | Demonstrates geometric scaling and repositioning of basic shapes. |
| `Bernoulli` | `Manim-Bernoulli.py` | Animates the compound interest formula `(1+r/n)^n` for r=0.05, 0.50, and 1.00 across n compounding intervals, showing each curve converging toward a limit and illustrating Bernoulli's discovery of `e`. |
| `CircleEquation` | `Manim-CircleEquation.py` | Draws the implicit circle `x^2 + y^2 = 1` on coordinate axes. |
| `ComplexPlaneEuler01` | `Manim-ComplexPlane-Euler01.py` | 3D Euler-formula visualization with `x` as input angle, `\sin(x)` in the `x-y` plane, `\cos(x)` in the `x-z` plane, and a red helix `(x, \sin x, \cos x)` showing their combined relationship. |
| `ComplexPlaneEuler02` | `Manim-ComplexPlane-Euler02.py` | Extends the Euler helix scene with a moving point on `(x, \sin x, \cos x)` that drops real-time projection dots and dashed guide lines to the `x-y` and `x-z` planes for clearer decomposition. |
| `ComplexPlaneEuler03` | `Manim-ComplexPlane-Euler03.py` | Animates the unit circle from `0` to `2\pi` with a rotating radius, dynamic right-triangle legs labeled `\cos(\theta)` and `\sin(\theta)`, a `\theta` angle marker at the origin, and a moving point labeled `e^{i\theta}` on the circle. |
| `ComplexPlane01` | `Manim-ComplexPlane01.py` | Draws the complex plane with `Re(s)` / `Im(s)` axes, shades the critical strip `0 < Re(s) < 1`, marks the critical line `Re(s) = 1/2` in yellow, then animates vertical lines transforming into parabolas under the mapping `f(z) = z²`. |
| `ComplexPlane02` | `Manim-ComplexPlane02.py` | Same complex plane framework; animates `f(z) = e^z` in two phases: vertical lines curl into concentric circles of radius `e^a`, then horizontal lines fan out into rays at angle `b` — together revealing the Cartesian-to-polar grid transformation. |
| `ComplexPlane03` | `Manim-ComplexPlane03.py` | Same complex plane framework; animates the inversion map `f(z) = 1/z` in two phases: vertical lines `Re(z)=a` collapse into circles centred on the real axis, then horizontal lines `Im(z)=b` collapse into circles centred on the imaginary axis — all circles pass through the origin. |
| `CosecantGraph` | `Manim-CosecantGraph.py` | Plots a cosecant-based trig graph with discontinuities and pi-labeled x-axis. |
| `CubicTangent` | `Manim-CubicTangent.py` | Animates motion along the cubic function `f(x)=x^3` (tangent-focused setup). |
| `CurveMinimum` | `Manim-CurveMinimum.py` | Tracks a point on a quadratic curve and moves it to the parabola's minimum. |
| `DerivativeLimit` | `Manim-DerivativeLimit.py` | Shows Riemann-sum convergence for `y=x^2` alongside exact integral area/error. |
| `Discontinuity` | `Manim-Discontinuity.py` | Shows a removable discontinuity (hole) in a rational function graph. |
| `EpsilonDelta` | `Manim-EpsilonDelta.py` | Visualizes epsilon-delta limit neighborhoods around `x=C` and `y=L` on a function graph. |
| `Fixed3DText` | `Manim-Fixed3DText.py` | 3D axes scene demonstrating fixed-in-frame text overlay. |
| `GaussianSurface` | `Manim-GaussianSurface.py` | Plots a Gaussian-like 3D surface over the `(x,y)` plane. |
| `IrrationalRoot2` | `Manim-Irrational-Root2.py` | Presents a step-by-step contradiction proof that `\sqrt{2}` is irrational, ending with the conclusion and historical caution note alluding to Hippasus. |
| `LitSphere` | `Manim-LitSphere.py` | 3D parametric surface scene with adjusted light-source position. |
| `ParabolaTangent` | `Manim-ParabolaTangent.py` | Draws a parabola with a tangent line at a selected point. |
| `PolarTangent` | `Manim-PolarTangent.py` | Uses polar coordinates to animate a point on a circle with tangent behavior. |
| `RadiusSweep` | `Manim-RadiusSweep.py` | Rotates a radius line around a circle to illustrate full-angle sweep. |
| `RiemannSum` | `Manim-RiemannSum.py` | Approximates area under `y=x^2` using left Riemann rectangles with decreasing `dx`. |
| `SigmoidFunc` | `Manim-SigmoidFunc.py` | Logistic sigmoid plot with displayed weight and bias values. |
| `SigmoidPlot` | `Manim-SigmoidPlot.py` | Plots the logistic sigmoid with configurable weight and bias parameters. |
| `SinCosTriangle` | `Manim-SinCosTriangle.py` | Animates radius rotation with dynamic sine/cosine triangle projections. |
| `SineCurve` | `Manim-SineCurve.py` | Basic sine curve plot over `[-pi, pi]`. |
| `SineWave` | `Manim-SineWave.py` | Graphs `sin(x)` over `[-pi, pi]` with key pi-based angle labels. |
| `SlopeField` | `Manim-SlopeField.py` | Builds slope fields for first-order differential equations (`dy/dx = -x/y`, `x+y`, `y`). |
| `TangentGraph` | `Manim-TangentGraph.py` | Tangent-function style graph with asymptote-safe clipping behavior. |
| `TaylorLn` | `Manim-TaylorLn.py` | Compares `ln(x)` with increasing-degree Taylor polynomial approximations around `C=2`. |
| `UnitCircle` | `Manim-UnitCircle.py` | Animates radius rotation on a unit circle with angle `theta` annotation. |
| `VolumeRevolution` | `Manim-VolumeRevolution.py` | 3D volume of revolution: plots `f(x)=4x²+5`, draws left Riemann rectangles (Δx=0.2) on `[2,4]`, then rotates both around the x-axis to illustrate the disc-method integral `V=π∫[f(x)]²dx`. |

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
