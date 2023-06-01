#!/bin/bash

git -C third_party clone https://github.com/ros-planning/navigation.git -b noetic-devel

git -C third_party clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git -b noetic-devel

git -C third_party clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel

git -C third_party clone https://github.com/5met4nka/gazebo_models_worlds_collection.git -b main

git -C third_party clone https://github.com/ros-controls/ros_controllers.git -b noetic-devel

git -C third_party clone https://github.com/ros-controls/ros_control.git -b noetic-devel

git -C third_party clone https://github.com/ros-drivers/four_wheel_steering_msgs.git -b master

git -C third_party clone https://github.com/ros-controls/urdf_geometry_parser.git -b kinetic-devel

git -C third_party clone https://github.com/ros/urdf.git -b melodic-devel

git -C third_party clone https://github.com/ros/joint_state_publisher.git -b noetic-devel

git -C third_party clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b noetic-devel

git -C third_party clone https://github.com/ros-drivers/joystick_drivers.git -b main

git -C third_party clone https://github.com/ros/geometry2.git -b noetic-devel

git -C third_party clone https://github.com/ros-teleop/teleop_tools.git -b noetic-devel

git -C third_party clone https://github.com/ros/robot_state_publisher.git -b noetic-devel