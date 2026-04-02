import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socket

ESP8266_IP = "192.168.117.XXX"  # ← ESP8266 IP
PORT = 90

class RosBridge(Node):
    def __init__(self):
        super().__init__('ros_bridge')
        
        self.subscription = self.create_subscription(
            String,
            'robot_cmd',
            self.callback,
            10
        )

    def callback(self, msg):
        try:
            s = socket.socket()
            s.connect((ESP8266_IP, PORT))
            s.send((msg.data + "\n").encode())
            s.close()

            self.get_logger().info(f'Sent: {msg.data}')

        except Exception as e:
            self.get_logger().error(f'Error: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = RosBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
