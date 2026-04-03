"""
test_scenes.py — Renders every Manim scene found in root-level Python files.

Usage:
    python tests/test_scenes.py [--quality {l,m,h}] [--log LOG_FILE]

Flags:
    --quality   Render quality: l (low, default), m (medium), h (high)
    --log       Path for the log file (default: tests/test_scenes.log)
"""

import ast
import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ── Manim scene base classes to recognise ────────────────────────────────────
SCENE_BASES = {
    "Scene",
    "ThreeDScene",
    "MovingCameraScene",
    "ZoomedScene",
    "VectorScene",
    "LinearTransformationScene",
    "SpecialThreeDScene",
    "SampleSpaceScene",
    "ReconfigurableScene",
}


def find_scene_classes(py_file: Path) -> list[str]:
    """Return a list of Manim scene class names defined in *py_file*."""
    try:
        tree = ast.parse(py_file.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return []

    scenes = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue
        for base in node.bases:
            base_name = ""
            if isinstance(base, ast.Name):
                base_name = base.id
            elif isinstance(base, ast.Attribute):
                base_name = base.attr
            if base_name in SCENE_BASES:
                scenes.append(node.name)
                break
    return scenes


def render_scene(py_file: Path, scene_class: str, quality_flag: str) -> tuple[bool, str]:
    """
    Run ``manim -q<quality> <file> <class>`` and return (success, output).
    Combines stdout + stderr so errors are always captured.
    """
    cmd = [sys.executable, "-m", "manim", f"-q{quality_flag}", str(py_file), scene_class]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def main():
    parser = argparse.ArgumentParser(description="Test-render all Manim scenes in the project root.")
    parser.add_argument("--quality", choices=["l", "m", "h"], default="l",
                        help="Render quality: l=low (default), m=medium, h=high")
    parser.add_argument("--log", default=None,
                        help="Log file path (default: tests/test_scenes.log)")
    args = parser.parse_args()

    tests_dir = Path(__file__).parent
    root = tests_dir.parent  # project root — one level up from tests/
    log_path = Path(args.log) if args.log else tests_dir / "test_scenes.log"

    # Collect root-level .py files, skipping hidden/venv dirs
    py_files = sorted(
        p for p in root.glob("*.py")
        if not any(part.startswith(".") for part in p.parts)
    )

    passed, failed, skipped = [], [], []
    start_time = time.time()

    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"Manim Scene Test Run — {datetime.now():%Y-%m-%d %H:%M:%S}\n")
        log.write(f"Quality: -{args.quality}  |  Root: {root}\n")
        log.write("=" * 72 + "\n\n")

        for py_file in py_files:
            scenes = find_scene_classes(py_file)

            if not scenes:
                msg = f"[SKIP]  {py_file.name}  (no Manim scene classes found)"
                print(msg)
                log.write(msg + "\n\n")
                skipped.append(py_file.name)
                continue

            for scene in scenes:
                label = f"{py_file.name}::{scene}"
                print(f"  Rendering {label} ...", end=" ", flush=True)
                t0 = time.time()
                ok, output = render_scene(py_file, scene, args.quality)
                elapsed = time.time() - t0

                if ok:
                    status = f"[PASS]  {label}  ({elapsed:.1f}s)"
                    print("PASS")
                    passed.append(label)
                else:
                    status = f"[FAIL]  {label}  ({elapsed:.1f}s)"
                    print("FAIL")
                    failed.append(label)

                log.write(status + "\n")
                if not ok:
                    log.write("-" * 60 + "\n")
                    log.write(output + "\n")
                    log.write("-" * 60 + "\n")
                log.write("\n")

        # ── Summary ──────────────────────────────────────────────────────────
        total_time = time.time() - start_time
        summary_lines = [
            "=" * 72,
            f"SUMMARY  ({total_time:.1f}s total)",
            f"  Passed : {len(passed)}",
            f"  Failed : {len(failed)}",
            f"  Skipped: {len(skipped)}",
        ]
        if failed:
            summary_lines.append("\nFailed scenes:")
            for f in failed:
                summary_lines.append(f"  - {f}")

        summary = "\n".join(summary_lines)
        log.write(summary + "\n")
        print("\n" + summary)

    print(f"\nFull log written to: {log_path}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
