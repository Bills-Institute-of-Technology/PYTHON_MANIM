from manim import *
import numpy as np
from fractions import Fraction


class IntroComplexGeometry0101(Scene):
    def construct(self):
        plane = ComplexPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=8,
            background_line_style={"stroke_opacity": 0.35},
        )
        plane.add_coordinates()

        re_label = MathTex(r"\Re", font_size=30).next_to(plane.x_axis.get_end(), RIGHT, buff=0.15)
        im_label = MathTex(r"\Im", font_size=30).next_to(plane.y_axis.get_end(), UP, buff=0.15)
        title = Text("Complex Point Sets and Arguments", font_size=26).to_corner(UL, buff=0.3)

        self.play(Create(plane), Write(re_label), Write(im_label), run_time=1.8)
        self.play(Write(title), run_time=1.0)

        point_sets = [
            (r"(1,\ i,\ -1,\ -i)", [1 + 0j, 0 + 1j, -1 + 0j, 0 - 1j]),
            (r"(0,\ 1+i,\ \sqrt{2}i,\ i-1)", [0 + 0j, 1 + 1j, 0 + np.sqrt(2) * 1j, -1 + 1j]),
            (r"(1+i,\ 1+2i,\ 2(i+1),\ 2+i)", [1 + 1j, 1 + 2j, 2 * (1 + 1j), 2 + 1j]),
        ]

        for set_text, values in point_sets:
            set_label = MathTex(set_text, font_size=28).to_corner(UR, buff=0.4)
            self.play(FadeIn(set_label), run_time=0.5)

            set_group = VGroup()
            point_entries = []

            for point_index, z in enumerate(values):
                point_group, arg_label = self._build_point_group(plane, z, point_index)
                set_group.add(point_group)
                point_entries.append((point_group, arg_label))

            previous_arg_label = None
            for point_group, arg_label in point_entries:
                if previous_arg_label is None:
                    self.play(Create(point_group), run_time=2)
                else:
                    self.play(
                        Create(point_group),
                        FadeOut(previous_arg_label),
                        run_time=2,
                    )
                previous_arg_label = arg_label

            self.wait(2)
            self.play(FadeOut(set_group), FadeOut(set_label), run_time=0.9)

        self.wait(0.6)

    def _build_point_group(self, plane: ComplexPlane, z: complex, point_index: int):
        origin = plane.n2p(0)
        z_point = plane.n2p(z)

        vector = Line(origin, z_point, color=YELLOW, stroke_width=2.6)
        dot = Dot(z_point, color=RED, radius=0.06)

        z_label = MathTex(self._complex_latex(z), font_size=28, color=RED)
        z_label.next_to(dot, UR, buff=0.12)

        point_group = VGroup(vector, dot, z_label)

        if abs(z) < 1e-9:
            arg_label = MathTex(r"\arg(0)\ \text{undefined}", font_size=24, color=GRAY_C)
            arg_label.next_to(dot, DOWN, buff=0.14)
            point_group.add(arg_label)
            return point_group, arg_label

        theta = np.angle(z)
        arc_radius = 0.32 + 0.08 * point_index
        arg_arc = Arc(
            radius=arc_radius,
            start_angle=0,
            angle=theta,
            arc_center=origin,
            color=BLUE_C,
            stroke_width=2.6,
        )

        theta_direction = np.array([
            np.cos(theta / 2),
            np.sin(theta / 2),
            0,
        ])
        arg_label = MathTex(
            rf"\arg(z)={self._angle_latex(theta)}",
            font_size=24,
            color=BLUE_C,
        )
        arg_label.move_to(origin + theta_direction * (arc_radius + 0.18))

        point_group.add(arg_arc, arg_label)
        return point_group, arg_label

    def _angle_latex(self, theta: float) -> str:
        while theta <= -np.pi:
            theta += TAU
        while theta > np.pi:
            theta -= TAU

        ratio = theta / np.pi
        approx = Fraction(ratio).limit_denominator(12)

        if abs(ratio - float(approx)) > 1e-5:
            return rf"{theta:.2f}"

        numerator = approx.numerator
        denominator = approx.denominator

        if numerator == 0:
            return "0"

        if denominator == 1:
            if numerator == 1:
                return r"\pi"
            if numerator == -1:
                return r"-\pi"
            return rf"{numerator}\pi"

        sign = "-" if numerator < 0 else ""
        abs_num = abs(numerator)

        if abs_num == 1:
            return rf"{sign}\frac{{\pi}}{{{denominator}}}"

        return rf"{sign}\frac{{{abs_num}\pi}}{{{denominator}}}"

    def _complex_latex(self, z: complex) -> str:
        x = z.real
        y = z.imag

        def fmt(v: float) -> str:
            if abs(v - round(v)) < 1e-9:
                return str(int(round(v)))
            frac = Fraction(v).limit_denominator(12)
            if abs(v - float(frac)) < 1e-5:
                if frac.denominator == 1:
                    return str(frac.numerator)
                return rf"\frac{{{frac.numerator}}}{{{frac.denominator}}}"
            return f"{v:.2f}"

        if abs(x) < 1e-9 and abs(y) < 1e-9:
            return "0"

        if abs(y) < 1e-9:
            return fmt(x)

        if abs(x) < 1e-9:
            if abs(y - 1) < 1e-9:
                return "i"
            if abs(y + 1) < 1e-9:
                return "-i"
            return rf"{fmt(y)}i"

        sign = "+" if y >= 0 else "-"
        ay = abs(y)

        if abs(ay - 1) < 1e-9:
            imag_part = "i"
        else:
            imag_part = rf"{fmt(ay)}i"

        return rf"{fmt(x)}{sign}{imag_part}"


# To render this scene:
# manim -pql Manim-IntroComplexGeometry0101.py IntroComplexGeometry0101
