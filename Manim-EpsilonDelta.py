from manim import *
import numpy as np

class EpsilonDelta(Scene):
    def construct(self):
        # Create the coordinate system
        axes = Axes(
            x_range=[-1, 10, 1],
            y_range=[-1, 10, 1],
            axis_config={"include_tip": False}
        )

        # Define the function
        def func(x):
            return (1/10) * ((x-2)*(x-5)*(x-8)) + 5

        # Create the function plot
        graph = axes.plot(
            func,
            x_range=[0.325, 9],
            color=BLUE
        )

        # Configurable C and L
        INITIAL_C = 5.0
        LINK_L_TO_FUNC = True  # If True, L follows f(C); set to False to control L independently
        INITIAL_L = 5.0        # Used only if LINK_L_TO_FUNC is False
        INITIAL_DELTA = 1.0    # Initial delta value for the epsilon-delta proof
        DISPLAY_Y_MIN = 0.0    # Clip delta-related visuals to [0, 10]
        DISPLAY_Y_MAX = 10.0
        DISPLAY_X_MIN = 0.0    # Clip epsilon-related visuals to [0, 10]
        DISPLAY_X_MAX = 10.0
        INITIAL_EPSILON = 1.0  # Initial epsilon value for the epsilon-delta proof

        c_tracker = ValueTracker(INITIAL_C)
        l_tracker = ValueTracker(INITIAL_L)
        delta_tracker = ValueTracker(INITIAL_DELTA)
        epsilon_tracker = ValueTracker(INITIAL_EPSILON)

        def current_L():
            return func(c_tracker.get_value()) if LINK_L_TO_FUNC else l_tracker.get_value()

        # Yellow vertical line x = C
        v_line = always_redraw(lambda: Line(
            start=axes.c2p(c_tracker.get_value(), DISPLAY_Y_MIN),
            end=axes.c2p(c_tracker.get_value(), DISPLAY_Y_MAX),
            color=YELLOW
        ))

        # Yellow horizontal line y = L
        h_line = always_redraw(lambda: Line(
            start=axes.c2p(DISPLAY_X_MIN, current_L()),
            end=axes.c2p(DISPLAY_X_MAX, current_L()),
            color=YELLOW
        ))

        # Labels for C and L
        label_C = always_redraw(lambda: MathTex("C", color=YELLOW).scale(0.6).next_to(v_line, UP, buff=0.2))
        label_L = always_redraw(lambda: MathTex("L", color=YELLOW).scale(0.6).next_to(h_line, RIGHT, buff=0.2))
        # |C - δ| label below the x = C line
        label_abs_C_delta = always_redraw(
            lambda: MathTex(r"\lvert C - \delta \rvert", color=YELLOW)
            .scale(0.6)
            .next_to(axes.c2p(c_tracker.get_value(), DISPLAY_Y_MIN), DOWN, buff=0.2)
        )
        # |L - ε| label left of the y-axis, aligned with y = L
        label_abs_L_epsilon = always_redraw(
            lambda: MathTex(r"\lvert L - \epsilon \rvert", color=YELLOW)
            .scale(0.6)
            .next_to(axes.c2p(DISPLAY_X_MIN, current_L()), LEFT, buff=0.2)
        )
        # f(x) label near the curve
        label_fx = MathTex("f(x)", color=BLUE).scale(0.6).next_to(axes.i2gp(8.5, graph), UR, buff=0.8)
        # Header in upper-left: If 0<|x-c|<δ then |f(x)-L|<ε
        header_limit_statement = MathTex(
            r"\text{if } 0<\lvert x - c \rvert < \delta \text{ then } \lvert f(x) - L \rvert < \epsilon",
            color=YELLOW
        ).scale(0.7).to_corner(UL, buff=0.4)
        header_limit_statement.shift(RIGHT * 0.4)

        # Intersection point of x = C with the curve y = f(C)
        intersection_dot = always_redraw(lambda: Dot(
            point=axes.c2p(c_tracker.get_value(), func(c_tracker.get_value())),
            radius=0.10,
            color=YELLOW
        ).set_z_index(2))

        # Delta area lines (left and right boundaries)
        delta_left_line = always_redraw(lambda: Line(
            start=axes.c2p(INITIAL_C - delta_tracker.get_value(), DISPLAY_Y_MIN),
            end=axes.c2p(INITIAL_C - delta_tracker.get_value(), DISPLAY_Y_MAX),
            color=RED
        ))
        
        delta_right_line = always_redraw(lambda: Line(
            start=axes.c2p(INITIAL_C + delta_tracker.get_value(), DISPLAY_Y_MIN),
            end=axes.c2p(INITIAL_C + delta_tracker.get_value(), DISPLAY_Y_MAX),
            color=RED
        ))

        # Hash pattern between the two delta lines (diagonal with positive slope)
        def make_hash_group():
            x_l = INITIAL_C - delta_tracker.get_value()
            x_r = INITIAL_C + delta_tracker.get_value()
            # For lines y = x + t, choose t so that the segment has some overlap with [DISPLAY_Y_MIN, DISPLAY_Y_MAX]
            t_start = DISPLAY_Y_MIN - x_r
            t_end = DISPLAY_Y_MAX - x_l
            spacing = 0.4
            group = VGroup()
            for t in np.arange(t_start, t_end, spacing):
                # Clip the diagonal segment to the horizontal band [DISPLAY_Y_MIN, DISPLAY_Y_MAX]
                # y = x + t intersects y=DISPLAY_Y_MIN at x = DISPLAY_Y_MIN - t; y=DISPLAY_Y_MAX at x = DISPLAY_Y_MAX - t
                x_start = max(x_l, DISPLAY_Y_MIN - t)
                x_end = min(x_r, DISPLAY_Y_MAX - t)
                if x_start < x_end:
                    y_start = x_start + t
                    y_end = x_end + t
                    group.add(Line(
                        start=axes.c2p(x_start, y_start),
                        end=axes.c2p(x_end, y_end),
                        color=RED,
                        stroke_width=2,
                        stroke_opacity=0.7
                    ))
            return group

        hash_group = always_redraw(make_hash_group)

        # Epsilon area lines (upper and lower boundaries)
        epsilon_lower_line = always_redraw(lambda: Line(
            start=axes.c2p(DISPLAY_X_MIN, current_L() - epsilon_tracker.get_value()),
            end=axes.c2p(DISPLAY_X_MAX, current_L() - epsilon_tracker.get_value()),
            color=RED
        ))
        
        epsilon_upper_line = always_redraw(lambda: Line(
            start=axes.c2p(DISPLAY_X_MIN, current_L() + epsilon_tracker.get_value()),
            end=axes.c2p(DISPLAY_X_MAX, current_L() + epsilon_tracker.get_value()),
            color=RED
        ))

        # Hash pattern between the two epsilon lines (diagonal with negative slope)
        def make_epsilon_hash_group():
            y_l = current_L() - epsilon_tracker.get_value()
            y_u = current_L() + epsilon_tracker.get_value()
            # For lines y = -x + t, choose t so that the segment has some overlap with [DISPLAY_X_MIN, DISPLAY_X_MAX]
            t_start = y_l + DISPLAY_X_MIN
            t_end = y_u + DISPLAY_X_MAX
            spacing = 0.4
            group = VGroup()
            for t in np.arange(t_start, t_end, spacing):
                # Clip the diagonal segment to the vertical band [DISPLAY_X_MIN, DISPLAY_X_MAX]
                # y = -x + t intersects x=DISPLAY_X_MIN at y = -DISPLAY_X_MIN + t; x=DISPLAY_X_MAX at y = -DISPLAY_X_MAX + t
                y_start = max(y_l, -DISPLAY_X_MAX + t)
                y_end = min(y_u, -DISPLAY_X_MIN + t)
                if y_start < y_end:
                    x_start = t - y_start
                    x_end = t - y_end
                    group.add(Line(
                        start=axes.c2p(x_start, y_start),
                        end=axes.c2p(x_end, y_end),
                        color=RED,
                        stroke_width=2,
                        stroke_opacity=0.7
                    ))
            return group

        epsilon_hash_group = always_redraw(make_epsilon_hash_group)

        # Add everything to the scene
        self.add(axes, graph, v_line, h_line, label_C, label_L, label_abs_C_delta, label_abs_L_epsilon, header_limit_statement, label_fx, intersection_dot, hash_group, delta_left_line, delta_right_line, epsilon_hash_group, epsilon_lower_line, epsilon_upper_line)
        
        # Animate delta and epsilon converging to 0 (lines converging to C and L)
        self.wait(1)  # Pause to show initial state
        self.play(
            delta_tracker.animate.set_value(0),
            epsilon_tracker.animate.set_value(0),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)  # Pause to show final converged state

# To render this scene:
# manim -pql Manim-EpsilonDelta.py EpsilonDelta