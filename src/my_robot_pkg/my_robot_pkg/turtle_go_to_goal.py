import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class GoToGoal(Node):
    def __init__(self):
        super().__init__('go_to_goal')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.target_x = 5.0
        self.target_y = 5.0

        self.current_pose = None

    def pose_callback(self, msg):
        self.current_pose = msg
        self.move_to_goal()

    def move_to_goal(self):
        if self.current_pose is None:
            return

        msg = Twist()

        dx = self.target_x - self.current_pose.x
        dy = self.target_y - self.current_pose.y

        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)

        angle_diff = angle - self.current_pose.theta

        # Control logic
        msg.linear.x = 1.5 * distance
        msg.angular.z = 4.0 * angle_diff

        self.publisher_.publish(msg)

        self.get_logger().info(f"Distance: {distance:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
