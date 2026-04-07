from manim import *
import numpy as np


class VolumeRevolution(ThreeDScene):
    def construct(self):
        # ─── Camera orientation ──────────────────────────────────────
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)

        # ─── Step 1: Draw 3-D axes ───────────────────────────────────
        # y/z ranges must accommodate max radius f(4)=69 after rotation
        axes = ThreeDAxes(
            x_range=[0, 5, 1],
            y_range=[0, 75, 15],
            z_range=[-75, 75, 15],
            x_length=5,
            y_length=4,
            z_length=4,
            axis_config={"include_tip": True, "color": BLUE},
        )
        x_label = axes.get_x_axis_label(MathTex("x"))
        y_label = axes.get_y_axis_label(MathTex("y"))

        self.play(Create(axes), run_time=1.5)
        self.play(Write(x_label), Write(y_label))
        self.wait(0.5)

        # HUD labels (fixed in camera frame)
        func_label = MathTex(r"f(x) = 4x^2 + 5", color=BLUE, font_size=36)
        func_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(func_label)
        self.play(Write(func_label))
        self.wait(0.3)

        # ─── Step 2: Animate f(x) curve in the x-y plane ────────────
        def f(x):
            return 4 * x**2 + 5

        curve = axes.plot(f, x_range=[2, 4], color=BLUE)
        self.play(Create(curve), run_time=2)
        self.wait(0.5)

        # ─── Step 3: Left Riemann rectangles (Δx = 0.2) ─────────────
        # x∈[2,4], 10 rectangles, heights evaluated at left endpoints
        dx = 0.2
        rects = VGroup()
        for x in np.arange(2, 4, dx):
            h = f(x)
            rect = Polygon(
                axes.c2p(x,      0, 0),
                axes.c2p(x + dx, 0, 0),
                axes.c2p(x + dx, h, 0),
                axes.c2p(x,      h, 0),
                fill_color=YELLOW,
                fill_opacity=0.5,
                stroke_color=WHITE,
                stroke_width=1.5,
            )
            rects.add(rect)

        self.play(
            LaggedStart(*[Create(r) for r in rects], lag_ratio=0.15),
            run_time=2,
        )
        self.wait(1)

        # ─── Step 4: Rotate curve + rectangles around the x-axis ────
        # Shift camera to a better perspective before rotating
        self.move_camera(phi=65 * DEGREES, theta=-40 * DEGREES, run_time=1.5)

        # Show the disc-method volume formula in the HUD
        vol_label = MathTex(
            r"V = \pi \int_2^4 \left[f(x)\right]^2 \, dx",
            font_size=30,
            color=WHITE,
        ).next_to(func_label, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(vol_label)
        self.play(Write(vol_label))
        self.wait(0.5)

        # Rotation axis = unit vector along the mathematical x-axis
        x_dir = axes.c2p(1, 0, 0) - axes.c2p(0, 0, 0)
        x_dir = x_dir / np.linalg.norm(x_dir)
        origin = axes.c2p(0, 0, 0)

        self.play(
            Rotate(curve, angle=2 * PI, axis=x_dir, about_point=origin),
            Rotate(rects, angle=2 * PI, axis=x_dir, about_point=origin),
            run_time=7,
            rate_func=linear,
        )
        self.wait(0.5)

        # ─── Step 5: Reveal the surface of revolution ────────────────
        # Parametric form: (u, v) → (u, f(u)·cos v, f(u)·sin v)
        rev_surface = Surface(
            lambda u, v: axes.c2p(u, f(u) * np.cos(v), f(u) * np.sin(v)),
            u_range=[2, 4],
            v_range=[0, TAU],
            resolution=(12, 32),
        )
        rev_surface.set_style(stroke_width=0.3, stroke_color=BLUE_E)
        rev_surface.set_fill_by_checkerboard(BLUE_D, BLUE_E, opacity=0.3)

        self.play(FadeIn(rev_surface), run_time=2)

        # Slow ambient rotation to show the 3-D volume from all sides
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()

# To render this scene:
# manim -pql Manim-VolumeRevolution.py VolumeRevolution
