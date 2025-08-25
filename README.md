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

## Recommended VS Code Extension

For a better development experience, install the **Manim Sideview** extension in VS Code. It provides live preview and integration for Manim projects.

- [Manim Sideview Extension](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview)

## Additional Notes

- Output videos and images are saved in the `media/` folder by default.
- For LaTeX rendering, ensure you have a working LaTeX distribution installed (e.g., MiKTeX or TeX Live).

---

For more information, see the [Manim documentation](https://docs.manim.community/).
