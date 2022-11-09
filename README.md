# Two Robot Navigation
### ASSIGNMENT BY [Aayush Vats](https://github.com/aayush11101998), [Subhransu Sourav Priyadarshan](https://github.com/subhransu10), [Azey Karimli](https://github.com/azaykarimli), [Alessandro Vaselli](https://github.com/Jellyfishh97)
### PROFESSOR ([Simone Macciò](https://github.com/SimoneMacci0))
## Pre-requisites
### Software required
1.) Gazebo ([about](https://gazebosim.org/home))

2.) RViz2 ([about](https://turtlebot.github.io/turtlebot4-user-manual/software/rviz.html#rviz2))

3.) Ros2 Galactic ([installation](http://docs.ros.org.ros.informatik.uni-freiburg.de/en/galactic/Installation.html))

4.) Navigation2 ([installation](https://navigation.ros.org/build_instructions/index.html))

### Robot Required
TURTLEBOT3 WAFFLE (use the command 'sudo apt-get install ros-(pkg_type)-turtlebot3-*')

### How to run
Before running make sure to `EXPORT` commands for Gazebo world models and robot models and `SOURCE` necessary commands.

on the terminal run "./run.sh" 

once the world is launched in the Gazebo give the initial position to the robots using the RViz select `2D pose Estimate` to give the initial position and then use `2D goal pose` to give the final goal to the robot.

## About
The `two_robot_nav` is a package where two robots use independent navigation2 package to navigate from a chosen initial point to a selected final point through the help of RViz2, avoiding collision from both static and moving objects.
###Some info about some important launch files:
([Bringup_Launch](https://github.com/aayush11101998/Sofar_assignment/blob/master/src/two_robot_nav/launch/bringup_launch.py)): Launches the navigation and Localization for the two robots.

([Rviz_launch](https://github.com/aayush11101998/Sofar_assignment/blob/master/src/two_robot_nav/launch/rviz_launch.py)): Launches the Rviz for robots.

([Multirobot_launch](https://github.com/aayush11101998/Sofar_assignment/blob/master/src/two_robot_nav/launch/multirobot_launch.py)): Launching this file launches tb3_launch file with different namespaced robots which satisfies the purpose of assignment i.e. functioning of multiple robots with independent navigation without collision.

([spawn_tb3_launch](https://github.com/aayush11101998/Sofar_assignment/blob/master/src/two_robot_nav/launch/spawn_tb3_launch.py)): Spawns the turtlebot_waffle.

([tb3_launch](https://github.com/aayush11101998/Sofar_assignment/blob/master/src/two_robot_nav/launch/tb3_launch.py)): Launches the spawn_tb3 along with gazebo environment and runs the bringup launch_file.

## NAV2 in Two robot navigation
Nav2 package is used here to navigate robot to a given destination using a certain set of task excecuting methods which are present in the Behavior Tree. This BT is consists of important functions like recovery function for the robot, computing a path, etc.

## Software architecture schematic graph
Below is a schematic diagram of the architecture used in the package

![Sofar Architecture](https://user-images.githubusercontent.com/91724060/200852701-1f94817d-455b-4505-b057-ada138b09aea.png)

*Note: Most relevent nodes are represented in this schematic diagram find a detailed version in the given ([link](https://github.com/aayush11101998/Sofar_assignment/blob/master/rosgraph.png)).

## Scope of improvements
More than two robots in the given package can be added just by editing the number of robots defined in the ([multirobot_launch](https://github.com/aayush11101998/Sofar_assignment/blob/master/src/two_robot_nav/launch/multirobot_launch.py)) and then just adding a parameter file in the `resource`. For n number of robots defined in the launch file define n number of parameter file for the robot.

Nodes to navigate robot through a script can be added in `two_robot_nav` of the package. 
!! Don't forget to mention the name of script in the setup.py.
 
