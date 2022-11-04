colcon build
source install/local_setup.bash
World_Models = $"sofar/sofar_assignment/src/multirobots_gazebo/world/models"
Turtlebot_models = $"opt/ros/galactic/share/turtlebot3_gazebo/models"
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$Turtlebot_models:$World_Models
export TURTLEBOT3_MODEL=waffle
ros2 launch two_robot_nav multirobot_launch.py 

