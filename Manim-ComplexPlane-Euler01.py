from manim import *
import numpy as np


class ComplexPlaneEuler01(ThreeDScene):
    def construct(self):
        # Camera setup
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        # 3D coordinate system: x (input angle), y (sin component), z (cos component)
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
        # note = Text("Helix from sine and cosine components", font_size=24).next_to(title, DOWN, aligned_edge=LEFT)

        self.add_fixed_in_frame_mobjects(title) #, note)

        # Curves on orthogonal planes
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

        # 3D helix (corkscrew) combining sine and cosine
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
        #self.play(Write(title), FadeIn(note), run_time=1.5)
        self.play(Write(title), run_time=1.5)

        self.play(Create(sin_curve), Write(sin_label), run_time=2)
        self.play(Create(cos_curve), Write(cos_label), run_time=2)
        self.play(Create(euler_helix), Write(helix_label), run_time=3)

        # Rotate slowly to emphasize 3D geometry
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait(1)


# To render this scene:
# manim -pql Manim-ComplexPlane-Euler01.py ComplexPlaneEuler01
