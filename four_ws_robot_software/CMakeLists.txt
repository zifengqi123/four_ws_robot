cmake_minimum_required(VERSION 2.8.3)
project(four_ws_robot_software)

find_package(catkin REQUIRED COMPONENTS
    amcl
    map_server
    move_base
    roscpp
    rospy
    topic_tools
)

catkin_package()

foreach(dir config/joy launch launch/joy worlds)
    install(DIRECTORY ${dir}/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

include_directories(
    ${catkin_INCLUDE_DIRS}
)