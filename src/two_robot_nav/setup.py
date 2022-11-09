from setuptools import setup

package_name = 'two_robot_nav'

data_files = []
data_files.append(('share/' + package_name + '/launch', ['launch/multirobot_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/spawn_tb3_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/rviz_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/tb3_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/localization_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/navigation_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/slam_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/bringup_launch.py']))
data_files.append(('share/' + package_name + '/launch', ['launch/nav_comm_robot_handler_launch.py']))

data_files.append(('share/' + package_name + '/resource', [
     'resource/nav2_default_view.rviz',
     'resource/nav2_multirobot_params_1.yaml',
     'resource/nav2_multirobot_params_2.yaml',
     'resource/nav2_namespaced_view.rviz',
     'resource/nav2_params.yaml',
     'resource/turtlebot3_waffle.urdf',
     'resource/turtlebot3_world.yaml',
     'resource/turtlebot3_world.pgm',
]))

data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/world', ['world/world.model']))
data_files.append(('share/' + package_name + '/world', ['world/waffle.model']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='subhransu10',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    keywords=['ROS2', 'Gazebo', 'Robot', 'Simulation', 'turtlebot3'],
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],
        'console_scripts': [
        ],
    },
)
