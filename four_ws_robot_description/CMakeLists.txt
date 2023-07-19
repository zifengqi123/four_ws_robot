cmake_minimum_required(VERSION 3.0.2)
project(four_ws_robot_description)

find_package(catkin REQUIRED COMPONENTS
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
