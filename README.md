# ROS-four_ws_navigation-src

create four_ws_navigation workspace

place four_ws_stage folder into /.gazebo/models directory

############navigation simulation#####
terminal1
$ source four_ws_navigation/devel/setup.bash
$ roslaunch robot_launch launch_navigation_simulation.launch

terminal2
$ source four_ws_navigation/devel/setup.bash
$ roslaunch navigation_params navigation.launch


############map creation##############
terminal1
$ source four_ws_navigation/devel/setup.bash
$ roslaunch robot_launch launch_simulation_for_map_creation.launch

terminal2
$ source four_ws_navigation/devel/setup.bash
$ rosrun gmapping slam_gmapping scan:=/front/scan

terminal3 (after the map created)
$ source four_ws_navigation/devel/setup.bash
$ rosrun map_server map_saver -f four_ws_map
