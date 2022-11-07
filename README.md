# Two Robot Navigation

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
The two robot navigation is a package where two robots use independent navigation2 package to navigate from a chosen initial point to a selected final point through the help of RViz2, avoiding collision from both static and moving objects.

## Software architecture schematic graph
Below is a schematic diagram of the architecture used in the package.
([image](link)) 

*Note: Most relevent nodes are represented in this schematic diagram find a detailed version in the given ([link](https://github.com/aayush11101998/Sofar_assignment/blob/master/rosgraph.png)). 
