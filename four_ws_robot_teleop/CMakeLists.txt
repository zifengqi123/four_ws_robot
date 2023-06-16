cmake_minimum_required(VERSION 3.0.2)
project(four_ws_robot_teleop)

find_package(catkin REQUIRED COMPONENTS
    geometry_msgs
    roscpp
    rospy
    sensor_msgs
    std_msgs
)

catkin_package()

include_directories()