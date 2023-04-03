cmake_minimum_required(VERSION 3.0.2)
project(gazebo_models_worlds_collection)
cmake_policy(SET CMP0054 NEW)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
)

find_package(gazebo REQUIRED)


catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS gazebo_ros
  DEPENDS GAZEBO
)

link_directories(${GAZEBO_LIBRARY_DIRS})

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

install(DIRECTORY launch models rviz worlds 
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
