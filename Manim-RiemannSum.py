from manim import *

class RiemannSum(Scene):
    def construct(self):
        # Define the function and interval
        func = lambda x: x**2
        interval = [0, 2]

        # Axes setup
        axes = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 5, 1],
            axis_config={"include_numbers": True}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Graph of the function
        graph = axes.plot(func, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="y = x^2")

        # Add axes and graph to the scene
        self.play(Create(axes), Write(labels))
        # Add the LaTeX formula
        formula = MathTex(r"\int_0^2 x^2 dx = \left[\frac{x^3}{3}\right]_0^2", font_size=36).to_edge(UP)
        self.play(Create(graph), Write(graph_label), Write(formula))

        # Riemann sum rectangles
        h_values = [0.25, 0.2, 0.15, 0.1, 0.05]
        for h in h_values:
            rectangles = axes.get_riemann_rectangles(
                graph=graph,
                x_range=interval,
                dx=h,
                input_sample_type="left",
                stroke_width=0.5,
                stroke_color=WHITE,
                fill_opacity=0.5
            )
            self.play(Create(rectangles))
            self.wait(1)
            self.play(FadeOut(rectangles))

        # End scene
        self.wait(2)

# To render this scene:
# manim -pql Manim-RiemannSum.py RiemannSum
