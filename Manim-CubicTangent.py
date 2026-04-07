from manim import *

class CubicTangent(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-30, 30, 3],
            axis_config={"color": BLUE}
        )

        # Define the function
        def func(x):
            return x**3

        # Create the graph of the function
        graph = axes.plot(func, color=YELLOW)

        # Create labels
        labels = axes.get_axis_labels(x_label="x", y_label="f(x) = x^3")

        # Create a dot to represent the point of tangency
        dot = Dot().move_to(axes.c2p(-3, func(-3)))

        # Create the tangent line
        #tangent_line = always_redraw(lambda: axes.get_tangent_line(
        #    graph,
        #    dot.get_center()[0],
        #    length=5, 
        #    color=RED
        #))
        
        # Create a ValueTracker to control the point on the curve
        alpha = ValueTracker(0.5)

        # Create the tangent line using always_redraw
        # tangent_line = always_redraw(lambda: TangentLine(
        #     graph, 
        #     dot.get_center()[0], 
        #     length=5, 
        #     color=RED
        # ))






        # Animate the graph, labels, dot, and tangent line
        self.play(Create(axes), Write(labels))
        self.play(Create(graph), run_time=2)
        #self.play(Create(dot), Create(tangent_line))
        # self.play(Create(dot))

        # Move the dot along the graph from x = -10 to x = 10
        self.play(dot.animate.move_to(axes.c2p(3, func(3))), run_time=5, rate_func=linear)
        self.wait()

# To render this scene:
# manim -pql Manim-CubicTangent.py CubicTangent
