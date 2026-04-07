from manim import *

class RadiusSweep(Scene):
    def construct(self):
        # Create the circle
        circle = Circle(radius=2, color=BLUE)  # Circle centered at origin, radius=2
        self.play(Create(circle))
        self.wait()

        # Create the radius line
        radius_line = Line(ORIGIN, circle.point_at_angle(0), color=YELLOW)

        # Add the radius line to the scene
        self.play(Create(radius_line))
        self.wait()

        # Animate the radius line rotating 360 degrees
        self.play(Rotate(radius_line, angle=2*PI, about_point=ORIGIN, run_time=4))
        self.wait()

# To render this scene:
# manim -pql Manim-RadiusSweep.py RadiusSweep
