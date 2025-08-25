from manim import *
import numpy as np

class CosecantSquaredGraph(Scene):
    def construct(self):
        # Create axes with pi units on x-axis
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/3],
            y_range=[-2, 2, 0.5],
            #x_axis_config={
            #    "numbers_to_include": [PI, 2*PI]
            #},
            axis_config={
                "color": BLUE,
                "include_numbers": False,
                "include_tip": True
            }
        )

        x_labels = [MathTex(r"-\pi"), MathTex("0"), MathTex(r"\pi")] 
        for label, x_coord in zip(x_labels, [-PI, 0, PI]):
            axes.add(label.next_to(axes.coords_to_point(x_coord, 0), DOWN))

        self.add(axes)

        # Add pi labels on x-axis
        x_labels = axes.get_x_axis_label("x")
        y_labels = axes.get_y_axis_label("y")
        
        # Function for csc^2(x)
        def csc_safe(x):
            # Avoid division by zero
            if (1.0/(np.sin(x)) > 2.0):
                return 2.0
            elif (1.0/(np.sin(x)) < -2.0):
                return -2.0
            
            return 1.0/(np.sin(x))
                
        def sin_func(x):
            return(np.sin(x))

        # Create the graph
        graph = axes.plot(
            csc_safe,
            discontinuities=[-2*PI, -3*PI/2, -PI, -PI/2, 0, PI/2, PI, 3*PI/2, 2*PI],
            dt=0.01,
            color=YELLOW
        )

        # Create the graph label
        graph_label = MathTex(r"f(x) = \csc(x)").next_to(axes, UP)

        # Animate everything
        self.play(Create(axes), Write(x_labels), Write(y_labels))
        self.play(Write(graph_label))
        self.play(Create(graph), run_time=3)
        self.wait(2)
