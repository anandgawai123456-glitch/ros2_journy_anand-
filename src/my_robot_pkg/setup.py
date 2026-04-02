from setuptools import find_packages, setup

package_name = 'my_robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        ('share/ament_index/resource_index/packages',
              ['resource/my_robot_pkg']),
        ('share/my_robot_pkg', ['package.xml']),
        ('share/my_robot_pkg/launch', ['launch/my_robot_launch.py']),

    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anand',
    maintainer_email='anand@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
      },
      entry_points={
        'console_scripts': [
            'publisher_node = my_robot_pkg.publisher_node:main',
            'subscriber_node = my_robot_pkg.subscriber_node:main',
            'turtle_controller = my_robot_pkg.turtle_controller:main',
            'temprature_publisher = my_robot_pkg.temprature_publisher:main',
            'temperature_subscriber = my_robot_pkg.temperature_subscriber:main',
            'temprature_subscriber = my_robot_pkg.temprature_subscriber:main',
            'temperature_service = my_robot_pkg.temperature_service:main',
            'robot_controller = my_robot_pkg.robot_controller:main', 
            'go_to_goal = my_robot_pkg.turtle_go_to_goal:main',
       ],

     },

   )

