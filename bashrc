#!/bin/bash

source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash

export CATKIN_WORKSPACE="$HOME/catkin_ws"
export GAZEBO_MODEL_PATH=$(rospack find maddrive_worlds)/models
