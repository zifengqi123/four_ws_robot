cmake_minimum_required(VERSION 2.8.3)
project(four_ws_robot_software)

find_package(catkin REQUIRED COMPONENTS
    rospy
)

catkin_package(
  INCLUDE_DIRS
  LIBRARIES
  CATKIN_DEPENDS
  DEPENDS
)

include_directories(
    ${catkin_INCLUDE_DIRS}
)
