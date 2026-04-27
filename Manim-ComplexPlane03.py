from manim import *
import numpy as np


class ComplexPlane03(Scene):
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

        # ─── f(z) = 1/z label ─────────────────────────────────────────────
        fz_label = MathTex(r"f(z) = \tfrac{1}{z}", font_size=34, color=ORANGE).to_corner(UR, buff=0.35)
        self.play(Write(fz_label))
        self.wait(0.3)

        # ─── Phase 1: Vertical lines → Circles (centred on real axis) ─────
        # Re(z) = a  ──1/z──►  circle centred at (1/(2a), 0), radius 1/(2|a|)
        # f(a + ti) = a/(a²+t²)  −  i·t/(a²+t²)
        map_note = MathTex(
            r"\text{vertical lines} \;\xrightarrow{\;1/z\;}\; \text{circles}",
            font_size=22, color=ORANGE,
        ).next_to(fz_label, DOWN, buff=0.2).to_edge(RIGHT, buff=0.4)

        vert_specs = [
            (-1.0, RED_C),
            (-0.5, TEAL_C),
            ( 0.5, GOLD),
            ( 1.0, BLUE_C),
        ]
        T_LINE = [-6.0, 6.0, 0.05]

        v_lines, v_circles = [], []
        for a, color in vert_specs:
            vline = ParametricFunction(
                lambda t, a=a: axes.c2p(a, t),
                t_range=T_LINE,
                color=color,
                stroke_width=2.5,
            )
            arc = ParametricFunction(
                lambda t, a=a: axes.c2p(
                    a / (a ** 2 + t ** 2),
                    -t / (a ** 2 + t ** 2),
                ),
                t_range=T_LINE,
                color=color,
                stroke_width=2.5,
            )
            v_lines.append(vline)
            v_circles.append(arc)

        self.play(*[Create(l) for l in v_lines], run_time=1.5)
        self.play(Write(map_note))
        self.wait(0.4)
        self.play(*[Transform(l, c) for l, c in zip(v_lines, v_circles)], run_time=2.5)
        self.wait(1)

        # ─── Phase 2: Horizontal lines → Circles (centred on imag axis) ───
        # Im(z) = b  ──1/z──►  circle centred at (0, −1/(2b)), radius 1/(2|b|)
        # f(t + bi) = t/(t²+b²)  −  i·b/(t²+b²)
        h_note = MathTex(
            r"\text{horizontal lines} \;\xrightarrow{\;1/z\;}\; \text{circles}",
            font_size=22, color=MAROON_B,
        ).next_to(fz_label, DOWN, buff=0.2).to_edge(RIGHT, buff=0.4)

        horiz_specs = [
            (-1.0, RED_C),
            (-0.5, TEAL_C),
            ( 0.5, GOLD),
            ( 1.0, BLUE_C),
        ]

        h_lines, h_circles = [], []
        for b, color in horiz_specs:
            hline = ParametricFunction(
                lambda t, b=b: axes.c2p(t, b),
                t_range=T_LINE,
                color=color,
                stroke_width=2.5,
            )
            arc = ParametricFunction(
                lambda t, b=b: axes.c2p(
                    t / (t ** 2 + b ** 2),
                    -b / (t ** 2 + b ** 2),
                ),
                t_range=T_LINE,
                color=color,
                stroke_width=2.5,
            )
            h_lines.append(hline)
            h_circles.append(arc)

        self.play(*[Create(l) for l in h_lines], run_time=1.5)
        self.play(Transform(map_note, h_note))
        self.wait(0.4)
        self.play(*[Transform(l, c) for l, c in zip(h_lines, h_circles)], run_time=2.5)
        self.wait(2)


# To render this scene:
# manim -pql Manim-ComplexPlane03.py ComplexPlane03
