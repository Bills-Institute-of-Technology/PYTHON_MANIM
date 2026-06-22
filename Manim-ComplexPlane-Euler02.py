from manim import *
import numpy as np


class ComplexPlaneEuler02(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            z_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            z_length=4,
            axis_config={"include_tip": True, "color": BLUE},
        )

        x_label = axes.get_x_axis_label(MathTex("x"))
        y_label = axes.get_y_axis_label(MathTex("\\sin(x)"))
        z_label = axes.get_z_axis_label(MathTex("\\cos(x)"))

        title = MathTex(r"e^{ix}=\cos(x)+i\sin(x)", font_size=40).to_edge(UP)
        projection_title = Text("Moving point with real-time projections", font_size=30).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        sin_curve = ParametricFunction(
            lambda t: axes.c2p(t, np.sin(t), 0),
            t_range=[0, 4 * PI],
            color=GREEN,
            stroke_width=4,
        )

        cos_curve = ParametricFunction(
            lambda t: axes.c2p(t, 0, np.cos(t)),
            t_range=[0, 4 * PI],
            color=YELLOW,
            stroke_width=4,
        )

        euler_helix = ParametricFunction(
            lambda t: axes.c2p(t, np.sin(t), np.cos(t)),
            t_range=[0, 4 * PI],
            color=RED,
            stroke_width=5,
        )

        sin_label = MathTex(r"y=\sin(x)", color=GREEN, font_size=30).move_to(axes.c2p(3 * PI, 1.2, 0.0))
        cos_label = MathTex(r"z=\cos(x)", color=YELLOW, font_size=30).move_to(axes.c2p(3 * PI, 0.0, 1.2))
        helix_label = MathTex(r"(x,\sin x,\cos x)", color=RED, font_size=30).move_to(axes.c2p(PI, -1.1, 1.0))

        self.play(Create(axes), Write(x_label), Write(y_label), Write(z_label), run_time=2)
        self.play(Write(title), run_time=1.5)
        self.play(Create(sin_curve), Write(sin_label), run_time=1.8)
        self.play(Create(cos_curve), Write(cos_label), run_time=1.8)
        self.play(Create(euler_helix), Write(helix_label), run_time=2.5)

        t_tracker = ValueTracker(0)

        moving_point = always_redraw(
            lambda: Dot(
                point=axes.c2p(
                    t_tracker.get_value(),
                    np.sin(t_tracker.get_value()),
                    np.cos(t_tracker.get_value()),
                ),
                radius=0.07,
                color=RED,
            )
        )

        xy_projection_dot = always_redraw(
            lambda: Dot(
                point=axes.c2p(
                    t_tracker.get_value(),
                    np.sin(t_tracker.get_value()),
                    0,
                ),
                radius=0.05,
                color=GREEN,
            )
        )

        xz_projection_dot = always_redraw(
            lambda: Dot(
                point=axes.c2p(
                    t_tracker.get_value(),
                    0,
                    np.cos(t_tracker.get_value()),
                ),
                radius=0.05,
                color=YELLOW,
            )
        )

        line_to_xy_plane = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(
                    t_tracker.get_value(),
                    np.sin(t_tracker.get_value()),
                    np.cos(t_tracker.get_value()),
                ),
                end=axes.c2p(
                    t_tracker.get_value(),
                    np.sin(t_tracker.get_value()),
                    0,
                ),
                color=GREEN,
                dash_length=0.08,
                stroke_width=3,
            )
        )

        line_to_xz_plane = always_redraw(
            lambda: DashedLine(
                start=axes.c2p(
                    t_tracker.get_value(),
                    np.sin(t_tracker.get_value()),
                    np.cos(t_tracker.get_value()),
                ),
                end=axes.c2p(
                    t_tracker.get_value(),
                    0,
                    np.cos(t_tracker.get_value()),
                ),
                color=YELLOW,
                dash_length=0.08,
                stroke_width=3,
            )
        )

        self.add_fixed_in_frame_mobjects(projection_title)
        self.play(ReplacementTransform(title, projection_title), run_time=1.2)

        self.add(line_to_xy_plane, line_to_xz_plane, xy_projection_dot, xz_projection_dot, moving_point)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.play(t_tracker.animate.set_value(4 * PI), run_time=10, rate_func=linear)
        self.stop_ambient_camera_rotation()
        self.wait(1)


# To render this scene:
# manim -pql Manim-ComplexPlane-Euler02.py ComplexPlaneEuler02
