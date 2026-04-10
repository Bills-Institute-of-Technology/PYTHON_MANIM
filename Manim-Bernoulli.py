from manim import *
import numpy as np


class Bernoulli(Scene):
    def construct(self):
        # ─── Axes ─────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 13, 1],
            y_range=[1.0, 3.0, 0.5],
            x_length=9,
            y_length=5.5,
            axis_config={"color": WHITE, "include_tip": False},
            x_axis_config={"numbers_to_include": [2, 4, 6, 8, 10, 12]},
            y_axis_config={"numbers_to_include": [1.0, 1.5, 2.0, 2.5, 3.0]},
        ).to_edge(LEFT, buff=0.3)

        x_label = axes.get_x_axis_label(MathTex(r"n"), direction=DOWN)

        self.play(Create(axes), Write(x_label))
        self.wait(0.5)

        # ─── Mathematician name label (UL corner) ─────────────────────
        name_label = Text("Bernoulli", color=BLUE_C, font_size=40, slant=ITALIC).to_corner(UL, buff=0.35)
        self.play(Write(name_label))

        # ─── Three curves: r = 0.05, 0.50, 1.00 (lighter → darker) ───
        curve_data = [
            (0.05, BLUE_B, r"f(n)=\left(1+\dfrac{0.05}{n}\right)^{n}"),
            (0.50, BLUE_D, r"f(n)=\left(1+\dfrac{0.50}{n}\right)^{n}"),
            (1.00, BLUE_E, r"f(n)=\left(1+\dfrac{1.00}{n}\right)^{n}"),
        ]

        formula_mob = None
        for r, color, tex in curve_data:
            new_label = MathTex(tex, color=color, font_size=30).to_edge(UP, buff=0.35)
            if formula_mob is None:
                self.play(Write(new_label))
                formula_mob = new_label
            else:
                self.play(Transform(formula_mob, new_label))

            curve = axes.plot(
                lambda x, r=r: (1 + r / x) ** x,
                x_range=[0.1, 12, 0.1],
                color=color,
                stroke_width=2.5,
            )
            self.play(Create(curve), run_time=2.5)
            self.wait(0.5)

        # ─── Horizontal line at y = e (asymptote for r = 1.00) ────────
        e_label = MathTex(
            r"e = \lim_{n \to \infty}\left(1+\frac{1}{n}\right)^{\!n} \approx 2.718",
            color=YELLOW,
            font_size=30,
        ).to_edge(UP, buff=0.35)
        euler_label = Text("Euler", color=YELLOW, font_size=40, slant=ITALIC).to_corner(UL, buff=0.35)
        self.play(Transform(formula_mob, e_label), Transform(name_label, euler_label))

        e_line = axes.plot(
            lambda x: np.e, x_range=[0.1, 12], color=YELLOW, stroke_width=2.5
        )
        e_tag = MathTex(r"y = e", color=YELLOW, font_size=26).next_to(
            axes.c2p(0.5, np.e), UP, buff=0.12
        )
        self.play(Create(e_line), run_time=2)
        self.play(Write(e_tag))
        self.wait(2)


# To render this scene:
# manim -pql Manim-Bernoulli.py Bernoulli
