from manim import *

class ParabolaTangent(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/3],
            y_range=[-2, 2, 0.5],
            axis_config={
                "color": BLUE,
                "include_numbers": False,
                "include_tip": True
            }
        )

        # Create a parabola function
        def parabola(x):
            return x**2

        graph = FunctionGraph(parabola, x_range=[-2, 2])

        # Create a tangent line at alpha=0.5 (middle of the parabola)
        tangent = TangentLine(graph, 0.75, length=1, color=RED)

        self.add(graph, tangent) 

        self.play(Create(axes))
        self.play(Create(graph), run_time=3)

# To render this scene:
# manim -pql Manim-ParabolaTangent.py ParabolaTangent
