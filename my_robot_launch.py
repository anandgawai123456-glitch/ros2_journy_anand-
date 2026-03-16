from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='my_robot_pkg',
            executable='temprature_publisher',
            name='temperature_publisher'
        ),

        Node(
            package='my_robot_pkg',
            executable='temprature_subscriber',
            name='temperature_subscriber'
        )

    ])
