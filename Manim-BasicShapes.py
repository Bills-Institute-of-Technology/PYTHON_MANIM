from manim import *

class SquareCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(circle))

class LabelUpdater(Scene):
    def construct(self):
        my_number = MathTex("ln(2)")
        my_box = always_redraw(lambda: SurroundingRectangle(my_number, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5))
        my_title = always_redraw(lambda: Tex("BillTech").next_to(my_box, DOWN, buff=0.25))

        self.play(Create(VGroup(my_number, my_box, my_title)))
        self.play(my_number.animate.shift(RIGHT * 2), run_time=2.0)
        self.wait()

class ShapeScaling(Scene):
     def contruct(self):
         my_title = Tex("Bills Institute of Technology").to_edge(UL,buff=0.5)

         my_square = Square(side_length=0.5, fill_color=BLUE).shift(LEFT * 3)
         my_triangle = Triangle().scale(0.6).to_edge(DR)

         self.play(Write(my_title))
         self.play(DrawBorderThenFill(my_square),run_time=2)
         self.play(Create(my_triangle))
         self.wait()

         self.play(my_title.animate.to_edge(UR),run_time=2)
         self.play(my_square.animate.scale(2), my_triangle.animate.to_edge(DL),run_time=3)
         self.wait()

# To render individual scenes from this file:
# manim -pql Manim-BasicShapes.py SquareCircle
# manim -pql Manim-BasicShapes.py LabelUpdater
# manim -pql Manim-BasicShapes.py ShapeScaling
