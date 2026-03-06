from manim import *
import numpy as np

class CustomTangentGraph(Scene):
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
        

        def safe_tan(x):
            if abs(x - np.pi/2) < 0.1 or abs(x + np.pi/2) < 0.1:
                return 1000  # Large value when close to asymptote
            return np.tan(x)

        tan_graph = self.get_graph(safe_tan, x_min=-2*np.pi, x_max=2*np.pi, color=RED)
        
        self.play(Create(axes))
        self.play(Create(tan_graph), run_time=2)
