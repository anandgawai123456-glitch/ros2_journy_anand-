import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

class TemperatureService(Node):

    def __init__(self):
        super().__init__('temperature_service')
        self.srv = self.create_service(Trigger, 'get_temperature', self.callback)
        self.get_logger().info("Temperature Service Ready")

    def callback(self, request, response):
        response.success = True
        response.message = "Temperature = 45C"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureService()
    rclpy.spin(node)
    rclpy.shutdown()
