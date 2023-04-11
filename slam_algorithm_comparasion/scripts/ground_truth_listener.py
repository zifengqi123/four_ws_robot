#!/usr/bin/env python

import os
import rospy
from nav_msgs.msg import Odometry

def callback_pose(data, file):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    file.write("{},{}\n".format(x, y))

def listener():
    rospy.init_node('ground_truth_listener', anonymous=False)
    workspace_path = os.environ['CATKIN_WORKSPACE']
    file_path = os.path.join(workspace_path, 'src/four_ws_robot/slam_algorithm_comparasion/ground_truth_listener.csv')
    with open(file_path, 'w') as file:
        file.write("x,y\n")  # записываем заголовок файла CSV
        rospy.Subscriber("/ground_truth/state", Odometry, callback_pose, file, queue_size=10)
        rospy.spin()

if __name__ == '__main__':
    listener()