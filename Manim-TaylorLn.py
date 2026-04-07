# Manim to demonstrate a Taylor Polynomial converging on natural log of X as the degree of the polynomal increases.
from manim import *
import numpy as np

class TaylorLn(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2, 4],
            y_range=[-2, 2],
            axis_config={
                "color": BLUE,
                "include_numbers": False,
                "include_tip": True
            }
        )

        # Yellow shades (brighter = higher values)
        colors = [
            "#FFFF00",  # Pure yellow
            "#FFFF33",  # Lighter
            "#FFFF66",  # Even lighter
            "#FFFF99",  # Very light yellow
            "#FFFFCC",  # Almost white-yellow
            "#FFFFFF"   # White
        ]
        # Or RGB: [(1, 1, 0), (1, 1, 0.2), (1, 1, 0.4), ...]

        # define the F(x)
        def Fx(x):
            return np.log(x)

        # Define the Taylor Polynomials for each degree
        #    THe nth degree polinomial could be done with recursion, adding flexiblity, but loosing clarity in the code
        #    numpy (mp) natural log is np.log(x), base 10 is log10(x) and base 2 is log2(x)
        C = 2

        def P_0(x):
            val = Fx(C)
            return np.where(x > 0, val, np.nan)
        
        def P_1(x):
            val = np.log(x) + (1/2)*(x-C)
            return np.where(x > 0, val, np.nan)

        def P_2(x):
            val = np.log(x) + (1/2)*(x-C) - (1/8)*(x-C)**2
            return np.where(x > 0, val, np.nan)

        def P_3(x):
            val = np.log(x) + (1/2)*(x-C) - (1/8)*(x-C)**2 + (1/24)*(x-C)**3
            return np.where(x > 0, val, np.nan)
        
        def P_4(x):
            val = np.log(x) + (1/2)*(x-C) - (1/8)*(x-C)**2 + (1/24)*(x-C)**3 - (1/64)*(x-C)**4
            return np.where(x > 0, val, np.nan)
        
        def P_5(x):
            val = np.log(x) + (1/2)*(x-C) - (1/8)*(x-C)**2 + (1/24)*(x-C)**3 - (1/64)*(x-C)**4 + (1/160)*(x-C)**5
            return np.where(x > 0, val, np.nan)

        # Note: Natural log is undefined for x <= 0, so start from a small positive value
        graph_ln_x = axes.plot(Fx, x_range=[0.135335283237, 4], color=RED)
        graph_P_0 = axes.plot(P_0, x_range=[0.135335283237, 4], color=colors[0])
        graph_P_1 = axes.plot(P_1, x_range=[0.31437, 4], color=colors[1])
        graph_P_2 = axes.plot(P_2, x_range=[0.41078, 4], color=colors[2])
        graph_P_3 = axes.plot(P_3, x_range=[0.45856, 4], color=colors[3])
        graph_P_4 = axes.plot(P_4, x_range=[0.48361, 4], color=colors[4])
        graph_P_5 = axes.plot(P_5, x_range=[0.49762, 4], color=colors[5])

        # draw the primay graph elements
        dot = Dot(color=YELLOW).move_to(axes.c2p(C, Fx(C))) # mark the center of the Taylor Polynomials
        self.add(axes)

        graph_label = MathTex(r"f(x)=ln(x) \: centered \: on \: C=2", font_size=24).to_edge(UL, buff=0.5)
        self.play(Create(graph_label),run_time=1)
        self.play(Create(graph_ln_x), run_time=2)
        self.add(dot)

        # Taylor Polynomial Degree 0
        #$P_0(x) = \mathbf{\ln(C)}$
        #P_0_label = MathTex(r"P_0: \: \mathbf{\ln(C)}", font_size=32,color=colors[0]).to_edge(DL, buff=0.5)
        #taylor_poly_eq = MathTex(r"P_0(x) = \ln(C)", font_size=24).to_edge(UL, buff=0.5).shift(DOWN*0.5)
        #self.add(taylor_poly_eq)
        self.play(Transform(graph_label, MathTex(r"P_0(x) = \ln(C)", font_size=24).to_edge(UL, buff=0.5)), run_time=1)
        self.play(Create(graph_P_0, run_time=2))

        # Taylor Polynomial Degree 1
        #$P_1(x) = \mathbf{\ln(C) + \frac{1}{2}(x-C)}$
        #P_1_label = MathTex(r"P_1: \: f(x)=\mathbf{\ln(C) + \frac{1}{2}(x-C)}", font_size=32,color=colors[1]).to_edge(DL, buff=0.1)
        self.play(Transform(graph_label, MathTex(r"P_1(x) = \ln(C) + \frac{1}{2}(x - C)", font_size=24).to_edge(UL, buff=0.5)), run_time=1)
        self.play(Create(graph_P_1, run_time=2))


        # Taylor Polynomial Degree 2
        #$P_2(x) = \mathbf{\ln(2) + \frac{1}{2}(x-2) - \frac{1}{8}(x-2)^2}$
        self.play(Transform(graph_label, MathTex(r"P_2(x) = \ln(C) + \frac{1}{2}(x - C) - \frac{1}{8}(x - C)^2", font_size=24).to_edge(UL, buff=0.5)), run_time=1)
        self.play(Create(graph_P_2, run_time=2))

        # Taylor Polynomial Degree 3
        #$P_3(x) = \mathbf{\ln(2) + \frac{1}{2}(x-2) - \frac{1}{8}(x-2)^2 + \frac{1}{24}(x-2)^3}$
        self.play(Transform(graph_label, MathTex(r"P_3(x) = \ln(C) + \frac{1}{2}(x - C) - \frac{1}{8}(x - C)^2 + \frac{1}{24}(x - C)^3", font_size=24).to_edge(UL, buff=0.5)), run_time=1)
        self.play(Create(graph_P_3, run_time=2))

        # Taylor Polynomial Degree 4
        #$P_4(x) = \mathbf{\ln(2) + \frac{1}{2}(x-2) - \frac{1}{8}(x-2)^2 + \frac{1}{24}(x-2)^3 - \frac{1}{64}(x-2)^4}$
        self.play(Transform(graph_label, MathTex(r"P_4(x) = \ln(C) + \frac{1}{2}(x - C) - \frac{1}{8}(x - C)^2 + \frac{1}{24}(x - C)^3 - \frac{1}{64}(x - C)^4", font_size=24).to_edge(UL, buff=0.5)), run_time=1)
        self.play(Create(graph_P_4, run_time=2))

        # Taylor Polynomial Degree 5
        #$P_5(x) = \mathbf{\ln(2) + \frac{1}{2}(x-2) - \frac{1}{8}(x-2)^2 + \frac{1}{24}(x-2)^3 - \frac{1}{64}(x-2)^4 + \frac{1}{160}(x-2)^5}$ [7, 8]  
        self.play(Transform(graph_label, MathTex(r"P_5(x) = \ln(C) + \frac{1}{2}(x - C) - \frac{1}{8}(x - C)^2 + \frac{1}{24}(x - C)^3 - \frac{1}{64}(x - C)^4 + \frac{1}{160}(x - C)^5", font_size=24).to_edge(UL, buff=0.5)), run_time=1)
        self.play(Create(graph_P_5, run_time=2))

# To render this scene:
# manim -pql Manim-TaylorLn.py TaylorLn
