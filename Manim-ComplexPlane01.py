from manim import *
import numpy as np


class ComplexPlane01(Scene):
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

        # ─── Animations ────────────────────────────────────────────────────
        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.3)

        self.play(FadeIn(critical_strip))
        self.play(
            Create(left_bound),
            Create(right_bound),
        )
        self.play(Write(strip_label))
        self.wait(0.3)

        self.play(Create(critical_line), run_time=1.2)
        self.play(Write(critical_label))
        self.wait(2)

        # ─── f(z) = z^2 label ─────────────────────────────────────────────
        fz_label = MathTex(r"f(z) = z^2", font_size=34, color=GREEN_C).to_corner(UR, buff=0.35)
        map_note = MathTex(
            r"\text{vertical lines} \;\xrightarrow{\;z^2\;}\; \text{parabolas}",
            font_size=22, color=GREEN_C,
        ).next_to(fz_label, DOWN, buff=0.2)

        self.play(Write(fz_label))
        self.wait(0.3)

        # ─── Build input vertical lines & output parabolas ─────────────────
        # For Re(z) = a: image is (a²−t², 2at). Clip t so output stays in [-6,6].
        curve_specs = [
            (-2, RED_C),
            (-1, GOLD),
            ( 1, GOLD),
            ( 2, RED_C),
        ]

        input_lines = []
        output_parabolas = []

        for a, color in curve_specs:
            t_max = min(6.0 / (2 * abs(a)), np.sqrt(a ** 2 + 6.0))
            t_rng = [-t_max, t_max, 0.05]

            vline = ParametricFunction(
                lambda t, a=a: axes.c2p(a, t),
                t_range=t_rng,
                color=color,
                stroke_width=2.5,
            )
            parabola = ParametricFunction(
                lambda t, a=a: axes.c2p(a ** 2 - t ** 2, 2 * a * t),
                t_range=t_rng,
                color=color,
                stroke_width=2.5,
            )
            input_lines.append(vline)
            output_parabolas.append(parabola)

        # Draw input lines
        self.play(*[Create(l) for l in input_lines], run_time=1.5)
        self.wait(0.4)
        self.play(Write(map_note))
        self.wait(0.4)

        # Transform each line into its parabolic image
        self.play(
            *[Transform(l, p) for l, p in zip(input_lines, output_parabolas)],
            run_time=2.5,
        )
        self.wait(2)


# To render this scene:
# manim -pql Manim-ComplexPlane01.py ComplexPlane01
