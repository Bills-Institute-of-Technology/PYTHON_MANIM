from manim import *

class CircleEquation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-1.1, 1.1, 1],
            axis_config={"color": BLUE},
            tips=False
        )

        # Scale the axes to make the Y-axis 75% larger
        axes.stretch(1.0, dim=1)  # dim=1 corresponds to the Y-axis

        # Create the circle graph
        circle = axes.plot_implicit_curve(
            lambda x, y: x**2 + y**2 - 1,
            color=YELLOW
        )

        # Create labels
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Add LaTeX label for the equation and position it at the top-right
        equation_label = MathTex(r"x^2 + y^2 = 1").to_edge(UL, buff=0.5)

        # Animate the graph
        self.play(Create(axes), Write(labels), Write(equation_label))
        self.play(Create(circle), run_time=2)
        self.wait()

# To render the scene, use the following command in your terminal:
# manim -pql Manim-Circle.py CircleEquation