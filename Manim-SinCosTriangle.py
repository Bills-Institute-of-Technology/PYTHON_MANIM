from manim import *

class SinCosTriangle(Scene):
    def construct(self):
        # Create the circle
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))
        self.wait()

        # Create the radius line
        radius_line = Line(ORIGIN, circle.point_at_angle(0), color=YELLOW)

        # Create sine and cosine lines
        sine_line = always_redraw(
            lambda: Line(
                radius_line.get_end(),  # From the tip of the radius line
                [radius_line.get_end()[0], 0, 0],  # Projected to x-axis (bottom of triangle)
                color=GREEN
            )
        )
        cosine_line = always_redraw(
            lambda: Line(
                ORIGIN,  # From the circle's center
                [radius_line.get_end()[0], 0, 0],  # Horizontal base on the x-axis
                color=RED
            )
        )

        # Add radius, sine, and cosine lines to the scene
        self.play(Create(radius_line))
        self.add(sine_line, cosine_line)
        self.wait()

        # Animate the radius line rotating around the circle
        self.play(Rotate(radius_line, angle=2 * PI, about_point=ORIGIN, run_time=6))
        self.wait()

# To render this scene:
# manim -pql Manim-SinCosTriangle.py SinCosTriangle
