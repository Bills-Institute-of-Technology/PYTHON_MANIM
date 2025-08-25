from manim import *
import numpy as np

class PolarCircle(Scene):
    def construct(self):
        # Create polar coordinate grid
        r_max = 3        
        
        polar_grid = PolarPlane(
            radius_max=r_max,
            size=r_max * 2,
            radius_step=1,
            #angle_step=PI/6,  # 30 degree steps in radians
            azimuth_step=12,
            azimuth_units="PI radians",
            azimuth_label_font_size=36,
            radius_config={"font_size": 36}
        ).add_coordinates()

        # Create circle path
        radius = 1
        circle = Circle(radius=radius, color=BLUE)

        # Function to get point on circle at given angle
        def get_circle_point(angle):
            return np.array([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ])
        
        def safe_tangent_length(theta):
            if (np.tan(theta) > 15.0):
                return 15.0
            else:
                return np.abs(np.tan(theta))

        # Function to get tangent line at given angle
        def get_tangent_line(angle):
            point = get_circle_point(angle)
            # Tangent direction is perpendicular to radius
            tangent_direction = np.array([
                -np.sin(angle),
                np.cos(angle),
                0
            ])
            # Create points for tangent line 
            if (angle >= 0 and angle <= PI/2):
                start_point = point - tangent_direction * safe_tangent_length(angle) # 2*radius
                end_point = point # + tangent_direction * 2*radius
            elif (angle > PI/2 and angle <= PI):
                start_point = point #- tangent_direction * 2*radius
                end_point = point + tangent_direction * safe_tangent_length(angle) # 2*radius
            elif (angle > PI and angle <= 3*PI/2):
                start_point = point - tangent_direction * safe_tangent_length(angle) # 2*radius
                end_point = point # + tangent_direction * 2*radius
            else:
                start_point = point # - tangent_direction * 2*radius
                end_point = point + tangent_direction * safe_tangent_length(angle) # 2*radius

            return Line(start_point, end_point, color=RED)

        # Initialize the point that will trace the circle
        tracing_dot = Dot(get_circle_point(0), color=YELLOW)
        initial_tangent = get_tangent_line(0)

        # Setup the scene
        # self.play(Create(polar_grid))
        self.add(polar_grid, circle)
        self.add(tracing_dot, initial_tangent)

        # Add circle drawing animation
        #self.play(Create(circle))
        #self.play(Create(tracing_dot), Create(initial_tangent))

        # Animate the dot and tangent line movement
        angle = ValueTracker(0)
        
        # Update function for dot position
        def update_dot(dot):
            current_angle = angle.get_value()
            dot.move_to(get_circle_point(current_angle))

        # Update function for tangent line
        def update_tangent(line):
            current_angle = angle.get_value()
            new_tangent = get_tangent_line(current_angle)
            line.become(new_tangent)

        # Add updaters
        tracing_dot.add_updater(update_dot)
        initial_tangent.add_updater(update_tangent)

        # Run the animation
        self.play(
            angle.animate.set_value(2*PI),
            rate_func=linear,
            run_time=8
        )

        # Remove updaters
        tracing_dot.remove_updater(update_dot)
        initial_tangent.remove_updater(update_tangent)

        #self.wait(2)
