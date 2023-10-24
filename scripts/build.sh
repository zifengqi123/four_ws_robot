#!/bin/bash

catkin build \
    four_ws_robot \
    four_wheel_steering_controller \
    swerve_steering_controller \
    four_wheel_steering_msgs \
    urdf_geometry_parser \
    geometry2 \
    hector_slam \
    hector_gazebo \
    maddrive_ros_shared \
    point_cloud_converter \
    -j$(($(nproc)-2))
