from manim import *
import numpy as np

class RiemannSumScene(Scene):
    def construct(self):
        # Add header text for limit definition of derivative
        header = MathTex(
            r"\text{Limit Definition of Derivative:}",
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}"
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(UP)
        
        # Set up the axes
        axes = Axes(
            x_range=[0, 2.2, 0.5],
            y_range=[0, 4.5, 1],
            axis_config={"include_tip": True},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create the function y = x^2
        def func(x):
            return x**2
        
        # Create the curve
        curve = axes.plot(func, x_range=[0, 2], color=BLUE)
        curve_label = MathTex("y = x^2").next_to(curve, UP, buff=0.2)
        
        # Add header first, then axes and curve to scene
        self.play(Write(header))
        self.wait()
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(curve), Write(curve_label))
        self.wait()

        # Function to create rectangles for a given step size
        def create_rectangles(h):
            rectangles = VGroup()
            x_vals = np.arange(0, 2, h)
            
            for x in x_vals:
                rect = axes.get_riemann_rectangles(
                    curve,
                    x_range=[x, x + h],
                    dx=h,
                    color=YELLOW,
                    fill_opacity=0.5
                )
                rectangles.add(rect)
            
            return rectangles

        # Create and animate rectangles for different step sizes
        step_sizes = [0.25, 0.1, 0.05]
        current_rectangles = None
        
        for h in step_sizes:
            new_rectangles = create_rectangles(h)
            
            # Calculate Riemann sum
            riemann_sum = sum([h * func(x) for x in np.arange(0, 2, h)])
            actual_area = 8/3  # ∫₀² x² dx = 8/3
            
            # Create text for current approximation
            sum_text = MathTex(
                f"h = {h}",
                f"\\text{{Approximation}} = {riemann_sum:.4f}",
                f"\\text{{Actual Area}} = {actual_area:.4f}",
                f"\\text{{Error}} = {abs(riemann_sum - actual_area):.4f}"
            ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT)
            
            if current_rectangles:
                self.play(
                    ReplacementTransform(current_rectangles, new_rectangles),
                    Write(sum_text)
                )
            else:
                self.play(
                    Create(new_rectangles),
                    Write(sum_text)
                )
            
            current_rectangles = new_rectangles
            self.wait(2)
            
            # Remove the sum text before next iteration
            if h != step_sizes[-1]:
                self.play(FadeOut(sum_text))
        
        # Final pause to show the most accurate approximation
        self.wait(2) 