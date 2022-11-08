colcon build
source install/local_setup.bash
World_Models = $(pwd)"src/multirobots_gazebo/world/models"
Turtlebot_models = $(pwd)"src/multirobots_gazebo/resource"
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$Turtlebot_models:$World_Models
export TURTLEBOT3_MODEL=waffle
ros2 launch two_robot_nav multirobot_launch.py 

