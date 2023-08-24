#!/bin/bash

catkin build \
    four_ws_robot \
    four_wheel_steering_msgs \
    gazebo_ros_pkgs \
    gazebo_ros_control \
    geometry2 \
    hector_slam \
    hector_imu_tools \
    joint_state_publisher \
    joint_state_publisher_gui \
    joystick_drivers \
    navigation \
    robot_state_publisher \
    ros_control \
    rqt_controller_manager \
    ros_controllers \
    four_wheel_steering_controller \
    slam_gmapping \
    urdf \
    urdf_geometry_parser \
    robot_localization \
    hector_gazebo \
    point_cloud_converter \
    twist_mux \
    maddrive_ros_shared \
    -j$(($(nproc)-2))
