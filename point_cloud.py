import open3d as o3d
from manim import *
from manim_slides import Slide
import random

class PointCloudPresentation(Slide, ThreeDScene):
    def construct(self):
        # Helper function to load a .ply file and convert it to a list of points
        def load_point_cloud(file_path, scale=0.4):
            pcd = o3d.io.read_point_cloud(file_path)
            points = [(scale * p[0], scale * p[1], scale * p[2]) for p in pcd.points]
            return points

        # Load .ply files
        point_cloud1 = load_point_cloud("data/partial/points_stump.ply", scale=0.5)
        point_cloud2 = load_point_cloud("data/partial/stump_after_density.ply", scale=0.5)
        point_cloud3 = load_point_cloud("data/partial/stump.ply", scale=0.5)

        # Create point groups for each point cloud
        points1 = VGroup(*[Dot3D(point=pos, color=BLUE, radius=0.04) for pos in point_cloud1])
        points2 = VGroup(*[Dot3D(point=pos, color=GREEN, radius=0.04) for pos in point_cloud2])
        points3 = VGroup(*[Dot3D(point=pos, color=RED, radius=0.04) for pos in point_cloud3])

        # Add axes
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-5, 5])
        self.add(axes)
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES, distance=4)

        # Slide 1: Show the first point cloud
        start_positions = [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for _ in point_cloud1]  # Define a far-away starting point
        flying_points = VGroup(*[Dot3D(point=pos, color=BLUE, radius=0.04) for pos in start_positions])
        self.add(flying_points)  # Add flying points off-screen
        self.play(Transform(flying_points, points1))  # Animate points flying to their positions
        self.begin_ambient_camera_rotation(rate=0.4)  # Start rotating the camera
        self.wait()
        self.next_slide()

        # Slide 2: Transition to the second point cloud
        self.play(Transform(flying_points, points2))
        self.wait()
        self.next_slide()

        # Slide 3: Transition to the third point cloud
        self.play(Transform(flying_points, points3))
        self.wait()
        self.stop_ambient_camera_rotation()
        self.next_slide()
