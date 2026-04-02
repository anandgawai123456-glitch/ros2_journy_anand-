import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.obstacle_detected = False

    def scan_callback(self, msg):
        # Check front distance
        front_distance = msg.ranges[0]

        if front_distance < 0.5:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

        self.move_robot()

    def move_robot(self):
        msg = Twist()

        if self.obstacle_detected:
            msg.linear.x = 0.0
            msg.angular.z = 0.5
            self.get_logger().info('Obstacle! Turning...')
        else:
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            self.get_logger().info('Moving Forward')

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
