from manim import *

class DiscontinuityScene01(Scene):
    def construct(self):
        # Create the coordinate system
        axes = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 10, 1],
            x_length=12,
            y_length=6,
            axis_config={"include_tip": True}
        ).scale(0.8)

        x_label, y_label = axes.get_axis_labels(x_label="x", y_label="f(x) = (x^2 - 9) / (x - 3)")

        def func(x):
            return (x**2 - 9) / (x - 3)
        
        graph = axes.plot(func, discontinuities=[3], x_range=[0.325, 6], color=BLUE)

        # Add a hollow circle at the discontinuity (x=3, y=6)
        discontinuity_x = 3
        discontinuity_y = 6  # limit as x->3
        hole = Circle(
            radius=0.08,
            color=BLUE,           # Outline color
            fill_color=BLACK,    # Fill color matches background
            fill_opacity=1       # Fully opaque fill
        ).move_to(axes.c2p(discontinuity_x, discontinuity_y))

        self.play(Create(axes), Create(x_label), Create(y_label))
        self.play(Create(graph),Create(hole))
        #self.play(Create(hole))
        self.wait(1)

        self.play(Create(axes), Create(x_label), Create(y_label))
        