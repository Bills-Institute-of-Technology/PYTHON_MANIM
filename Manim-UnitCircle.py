from manim import *
import numpy as np

class UnitCircle(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-2.0, 2.0, 1.0],
            y_range=[-2.0, 2.0, 1.0],
            axis_config={"color": BLUE},
            tips=False
        )

        axes.stretch(2.0, dim=1)  # Stretch the Y-axis for better proportions

        # Create the unit circle using axes scaling
        circle = Circle(
            radius=axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0],  # Radius in terms of axes scaling
            color=GREEN
        ).move_to(axes.c2p(0, 0))  # Center the circle at the origin of the axes

        # Add labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Add a line representing the radius
        radius_line = Line(axes.c2p(0, 0), axes.c2p(1, 0), color=RED)

        # Add a dot to indicate the moving point on the circle
        moving_dot = Dot(axes.c2p(1, 0), color=RED)

        # Add an angle arc and label
        angle_arc = always_redraw(
            lambda: Arc(
                radius=0.5,
                start_angle=0,
                angle=radius_line.get_angle(),
                color=YELLOW
            )
        )
        angle_label = always_redraw(
            lambda: MathTex(r"\theta").next_to(angle_arc, RIGHT, buff=0.1)
        )

        # Animate the angle θ from 0 to 2π
        self.play(Create(axes), Write(labels))
        self.play(Create(circle))
        self.play(Create(radius_line), Create(moving_dot))
        self.add(angle_arc, angle_label)

        self.play(
            Rotate(radius_line, angle=2 * PI, about_point=axes.c2p(0, 0)),
            MoveAlongPath(moving_dot, circle),
            run_time=6,
            rate_func=linear
        )
        self.wait()

# To render the scene, use the following command in your terminal:
# manim -pql Manim-UnitCircle.py UnitCircle