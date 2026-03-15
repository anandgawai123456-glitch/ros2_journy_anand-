from setuptools import find_packages, setup

package_name = 'my_robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
         ],

      },

   )

