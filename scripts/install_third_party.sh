#!/bin/bash

THIRD_PARTY_DIR=third_party
mkdir -p $THIRD_PARTY_DIR

git -C $THIRD_PARTY_DIR clone https://github.com/ros-planning/navigation.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/MarkNaeem/ros_controllers.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-controls/ros_control.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-drivers/four_wheel_steering_msgs.git -b master

git -C $THIRD_PARTY_DIR clone https://github.com/ros-controls/urdf_geometry_parser.git -b kinetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros/urdf.git -b melodic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros/joint_state_publisher.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-drivers/joystick_drivers.git -b main

git -C $THIRD_PARTY_DIR clone https://github.com/ros/geometry2.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros/robot_state_publisher.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/cra-ros-pkg/robot_localization.git -b noetic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-teleop/twist_mux.git -b melodic-devel

git -C $THIRD_PARTY_DIR clone https://github.com/ros-geographic-info/geographic_info.git -b master

git -C $THIRD_PARTY_DIR clone https://github.com/ros-geographic-info/unique_identifier.git -b master
