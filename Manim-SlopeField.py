from manim import *
import numpy as np

class SlopeField(Scene):
    def construct(self):
        # Configure for 1080x1080 square format
        config.frame_width = 8
        config.frame_height = 8
        
        # Create axes with equal scaling for square format
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={
                "color": BLUE,
                "include_numbers": False,
                "include_tip": True
            },
            x_length=7,  # Adjusted for square format
            y_length=7   # Adjusted for square format
        )

        # Function to calculate slope at a point (x, y) for different DEs
        def get_slope(x, y, de_type):
            if de_type == 1:  # dy/dx = -x/y
                if y == 0:
                    return float('inf')  # Vertical line
                return -x / y
            elif de_type == 2:  # dy/dx = x + y
                return x + y
            elif de_type == 3:  # dy/dx = y
                return y
            return 0

        # Function to create a line segment at a point
        def create_slope_segment(x, y, length=0.3, de_type=1):
            slope = get_slope(x, y, de_type)
            
            if slope == float('inf'):
                # Vertical line
                start_point = axes.coords_to_point(x, y - length/2)
                end_point = axes.coords_to_point(x, y + length/2)
            else:
                # Calculate points for the line segment
                dx = length / (2 * np.sqrt(1 + slope**2))
                dy = slope * dx
                
                start_point = axes.coords_to_point(x - dx, y - dy)
                end_point = axes.coords_to_point(x + dx, y + dy)
            
            return Line(start_point, end_point, color=RED, stroke_width=2)

        # Define the points to visit in clockwise order for each box
        # Box 1: (-1,1) to (1,1)
        box1_points = [
            (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)
        ]
        
        # Box 2: (-2,-2) to (2,2) - excluding points already in box1
        box2_points = [
            (2, 2), (2, 1), (2, 0), (2, -1), (2, -2),
            (1, -2), (0, -2), (-1, -2), (-2, -2),
            (-2, -1), (-2, 0), (-2, 1), (-2, 2),
            (-1, 2), (0, 2), (1, 2)
        ]
        
        # Box 3: (-3,-3) to (3,3) - excluding points already in box1 and box2
        box3_points = [
            (3, 3), (3, 2), (3, 1), (3, 0), (3, -1), (3, -2), (3, -3),
            (2, -3), (1, -3), (0, -3), (-1, -3), (-2, -3), (-3, -3),
            (-3, -2), (-3, -1), (-3, 0), (-3, 1), (-3, 2), (-3, 3),
            (-2, 3), (-1, 3), (0, 3), (1, 3), (2, 3)
        ]

        # Combine all points in order
        all_points = box1_points + box2_points + box3_points

        # Define titles for each differential equation
        titles = [
            Text("dy/dx = -x/y", font_size=36, color=WHITE),
            Text("dy/dx = x + y", font_size=36, color=WHITE),
            Text("dy/dx = y", font_size=36, color=WHITE)
        ]
        
        for title in titles:
            title.to_edge(UL)

        # Show axes
        self.play(Create(axes))
        self.wait(1)

        # Animate all three differential equations
        for de_type in range(1, 4):
            # Show title for current DE
            self.play(Write(titles[de_type-1]))
            self.wait(0.5)
            
            # Animate slope field segments for current DE
            segments = []
            for i, (x, y) in enumerate(all_points):
                segment = create_slope_segment(x, y, de_type=de_type)
                segments.append(segment)
                
                # Create the segment
                self.play(Create(segment), run_time=0.1)
                
                # Add a small pause every few segments for visual clarity
                if (i + 1) % 8 == 0:
                    self.wait(0.2)
            
            # Pause to show completed slope field
            self.wait(2)
            
            # Clear slope field for next DE (except for the last one)
            if de_type < 3:
                self.play(FadeOut(Group(*segments)), FadeOut(titles[de_type-1]))
                self.wait(0.5)

# To render the scene, use the following command in your terminal:
# manim -pql Manim-SlopeField.py SlopeField