from manim import *
import numpy as np


class ComplexPlane02(Scene):
    def construct(self):
        # ─── Axes ─────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=9,
            y_length=7,
            axis_config={"color": WHITE, "include_tip": True},
            x_axis_config={
                "numbers_to_include": [-6, -4, -2, 0, 2, 4, 6],
            },
            y_axis_config={
                "numbers_to_include": [-6, -4, -2, 2, 4, 6],
            },
        )

        x_label = axes.get_x_axis_label(
            MathTex(r"\Re(s)", font_size=36), direction=RIGHT + DOWN * 0.3
        )
        y_label = axes.get_y_axis_label(
            MathTex(r"\Im(s)", font_size=36), direction=UP
        )

        # ─── Critical strip shading (0 < Re(s) < 1) ───────────────────────
        strip_corners = [
            axes.c2p(0, -6),
            axes.c2p(1, -6),
            axes.c2p(1,  6),
            axes.c2p(0,  6),
        ]
        critical_strip = Polygon(
            *strip_corners,
            fill_color=BLUE,
            fill_opacity=0.15,
            stroke_width=0,
        )

        # ─── Boundary lines at Re(s) = 0 and Re(s) = 1 ────────────────────
        left_bound = DashedLine(
            axes.c2p(0, -6), axes.c2p(0, 6), color=BLUE_B, stroke_width=1.5
        )
        right_bound = DashedLine(
            axes.c2p(1, -6), axes.c2p(1, 6), color=BLUE_B, stroke_width=1.5
        )

        # ─── Critical line at Re(s) = 1/2 ─────────────────────────────────
        critical_line = Line(
            axes.c2p(0.5, -6), axes.c2p(0.5, 6), color=YELLOW, stroke_width=2.5
        )
        critical_label = MathTex(
            r"\Re(s) = \tfrac{1}{2}", color=YELLOW, font_size=28
        ).next_to(axes.c2p(0.5, 6), UP, buff=0.15)

        # ─── Strip label ───────────────────────────────────────────────────
        strip_label = MathTex(
            r"0 < \Re(s) < 1", color=BLUE_C, font_size=26
        ).move_to(axes.c2p(0.5, -5))

        # ─── Title ─────────────────────────────────────────────────────────
        title = Text("The Complex Plane", font_size=27, color=WHITE).to_corner(UL, buff=0.3)

        # ─── Plane setup animations ────────────────────────────────────────
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.3)

        self.play(FadeIn(critical_strip))
        self.play(Create(left_bound), Create(right_bound))
        self.play(Write(strip_label))
        self.wait(0.3)

        self.play(Create(critical_line), run_time=1.2)
        self.play(Write(critical_label))
        self.wait(1)

        # ─── f(z) = e^z label ─────────────────────────────────────────────
        fz_label = MathTex(r"f(z) = e^z", font_size=34, color=GREEN_C).to_corner(UR, buff=0.35)
        self.play(Write(fz_label))
        self.wait(0.3)

        # ─── Phase 1: Vertical lines → Circles ────────────────────────────
        # Re(z) = a  ──e^z──►  circle of radius e^a centred at origin
        map_note = MathTex(
            r"\text{vertical lines} \;\xrightarrow{\;e^z\;}\; \text{circles}",
            font_size=22, color=GREEN_C,
        ).next_to(fz_label, DOWN, buff=0.2).to_edge(RIGHT, buff=0.4)

        vert_specs = [
            (-1.0, BLUE_C),
            ( 0.0, TEAL_C),
            ( 1.0, GREEN_B),
            ( 1.5, GOLD),
        ]
        T_CIRC = [-np.pi, np.pi, 0.05]

        v_lines, v_circles = [], []
        for a, color in vert_specs:
            vline = ParametricFunction(
                lambda t, a=a: axes.c2p(a, t),
                t_range=T_CIRC,
                color=color,
                stroke_width=2.5,
            )
            circle = ParametricFunction(
                lambda t, a=a: axes.c2p(np.exp(a) * np.cos(t), np.exp(a) * np.sin(t)),
                t_range=T_CIRC,
                color=color,
                stroke_width=2.5,
            )
            v_lines.append(vline)
            v_circles.append(circle)

        self.play(*[Create(l) for l in v_lines], run_time=1.5)
        self.play(Write(map_note))
        self.wait(0.4)
        self.play(*[Transform(l, c) for l, c in zip(v_lines, v_circles)], run_time=2.5)
        self.wait(1)

        # ─── Phase 2: Horizontal lines → Rays ─────────────────────────────
        # Im(z) = b  ──e^z──►  ray at angle b from origin
        # t range chosen so ray radii span e^-2 to e^1.7 ≈ 5.5 (within axes)
        ray_note = MathTex(
            r"\text{horizontal lines} \;\xrightarrow{\;e^z\;}\; \text{rays}",
            font_size=22, color=MAROON_B,
        ).next_to(fz_label, DOWN, buff=0.2).to_edge(RIGHT, buff=0.4)

        T_RAY = [-2.0, 1.7, 0.05]

        horiz_specs = [
            (           0, RED_C),
            (  np.pi / 4,  ORANGE),
            (  np.pi / 2,  YELLOW),
            (3*np.pi / 4,  GREEN_C),
            (     np.pi,   TEAL_C),
            ( -np.pi / 4,  PINK),
            ( -np.pi / 2,  PURPLE_B),
            (-3*np.pi / 4, MAROON_B),
        ]

        h_lines, h_rays = [], []
        for b, color in horiz_specs:
            hline = ParametricFunction(
                lambda t, b=b: axes.c2p(t, b),
                t_range=T_RAY,
                color=color,
                stroke_width=2.5,
            )
            ray = ParametricFunction(
                lambda t, b=b: axes.c2p(np.exp(t) * np.cos(b), np.exp(t) * np.sin(b)),
                t_range=T_RAY,
                color=color,
                stroke_width=2.5,
            )
            h_lines.append(hline)
            h_rays.append(ray)

        self.play(*[Create(l) for l in h_lines], run_time=1.5)
        self.play(Transform(map_note, ray_note))
        self.wait(0.4)
        self.play(*[Transform(l, r) for l, r in zip(h_lines, h_rays)], run_time=2.5)
        self.wait(2)


# To render this scene:
# manim -pql Manim-ComplexPlane02.py ComplexPlane02
