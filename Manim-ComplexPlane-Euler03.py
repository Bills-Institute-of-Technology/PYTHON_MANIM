from manim import *
import numpy as np


class ComplexPlaneEuler03(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1.4, 1.4, 0.5],
            y_range=[-1.4, 1.4, 0.5],
            x_length=7,
            y_length=7,
            axis_config={"color": BLUE, "include_tip": True},
            tips=True,
        )

        x_label = axes.get_x_axis_label(MathTex("x"))
        y_label = axes.get_y_axis_label(MathTex("y"))

        title = MathTex(r"e^{i\theta}=\cos(\theta)+i\sin(\theta)", font_size=40).to_edge(UL)

        theta_tracker = ValueTracker(0)

        def circle_point(theta):
            return axes.c2p(np.cos(theta), np.sin(theta))

        origin = axes.c2p(0, 0)

        radius_line = always_redraw(
            lambda: Line(origin, circle_point(theta_tracker.get_value()), color=YELLOW, stroke_width=4)
        )

        circle_trace = always_redraw(
            lambda: ParametricFunction(
                lambda t: circle_point(t),
                t_range=[0, max(1e-3, theta_tracker.get_value())],
                color=WHITE,
                stroke_width=4,
            )
        )

        moving_dot = always_redraw(
            lambda: Dot(circle_point(theta_tracker.get_value()), color=RED, radius=0.07)
        )

        horizontal_arm = always_redraw(
            lambda: Line(
                origin,
                axes.c2p(np.cos(theta_tracker.get_value()), 0),
                color=GREEN,
                stroke_width=4,
            )
        )

        vertical_arm = always_redraw(
            lambda: Line(
                axes.c2p(np.cos(theta_tracker.get_value()), 0),
                circle_point(theta_tracker.get_value()),
                color=ORANGE,
                stroke_width=4,
            )
        )

        cos_label = always_redraw(
            lambda: MathTex(r"\cos(\theta)", color=GREEN, font_size=30).move_to(
                axes.c2p(np.cos(theta_tracker.get_value()) / 2, -0.12)
            )
        )

        sin_label = always_redraw(
            lambda: MathTex(r"\sin(\theta)", color=ORANGE, font_size=30).move_to(
                axes.c2p(
                    np.cos(theta_tracker.get_value()) + 0.16,
                    np.sin(theta_tracker.get_value()) / 2,
                )
            )
        )

        theta_arc = always_redraw(
            lambda: Arc(
                radius=0.4 * axes.x_axis.get_unit_size(),
                start_angle=0,
                angle=theta_tracker.get_value(),
                arc_center=origin,
                color=YELLOW,
                stroke_width=3,
            )
        )

        theta_label = always_redraw(
            lambda: MathTex(r"\theta", color=YELLOW, font_size=30).move_to(
                origin
                + 0.52 * axes.x_axis.get_unit_size() * np.array([
                    np.cos(theta_tracker.get_value() / 2),
                    np.sin(theta_tracker.get_value() / 2),
                    0,
                ])
            )
        )

        point_label = always_redraw(
            lambda: MathTex(r"e^{i\theta}", color=RED, font_size=30).next_to(moving_dot, UR, buff=0.12)
        )

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.8)
        self.play(Write(title), run_time=1.2)

        self.add(circle_trace, horizontal_arm, vertical_arm, radius_line, moving_dot)
        self.add(theta_arc, theta_label, cos_label, sin_label, point_label)

        self.play(theta_tracker.animate.set_value(TAU), run_time=10, rate_func=linear)
        self.wait(1)


# To render this scene:
# manim -pql Manim-ComplexPlane-Euler03.py ComplexPlaneEuler03
