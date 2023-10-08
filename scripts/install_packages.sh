#!/bin/bash

sudo apt install \
    ros-$ROS_DISTRO-move-base \
    ros-$ROS_DISTRO-amcl \
    ros-$ROS_DISTRO-gmapping \
    ros-$ROS_DISTRO-map-server \
    libspnav-dev
