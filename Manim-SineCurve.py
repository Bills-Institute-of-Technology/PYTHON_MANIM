from manim import *

class SineCurve(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-PI, PI, PI/4],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE}
        )

        # Create sine function graph
        sine_graph = axes.plot(lambda x: np.sin(x), color=ORANGE)

        # Create labels
        labels = axes.get_axis_labels(x_label="x", y_label="sin(x)")

        # Animate the graph
        self.play(Create(axes), Write(labels))
        self.play(Create(sine_graph), run_time=2)
        self.wait()

# To render this scene:
# manim -pql Manim-SineCurve.py SineCurve