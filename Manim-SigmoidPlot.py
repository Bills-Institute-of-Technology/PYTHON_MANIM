from manim import *

class SigmoidPlot(Scene):
    def construct(self):
        # Define weight and bias
        weight = 1
        bias = 0.25

        # Sigmoid function
        def sigmoid(x):
            return 1 / (1 + np.exp(-(weight * x + bias)))

        weight_text = MathTex("Weight:" + str(weight)).to_edge(UL).shift([0.25,-0.25,0.0])
        bias_text = MathTex("Bias: " + str(bias)).to_edge(UL).shift([0.25,-0.75,0.0])

        # Create axes
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-0.5, 1.5, 0.5],
            axis_config={"color": BLUE}
        )

        # Create sigmoid function graph
        sigmoid_graph = axes.plot(sigmoid, color=YELLOW)

        # Create labels
        labels = axes.get_axis_labels(x_label="x", y_label="sigmoid(x)")

        # Animate the graph
        self.play(Write(weight_text))
        self.play(Write(bias_text))

        self.play(Create(axes), Write(labels))
        self.play(Create(sigmoid_graph), run_time=2)
        self.wait()

# To render this scene:
# manim -pql Manim-SigmoidPlot.py SigmoidPlot
