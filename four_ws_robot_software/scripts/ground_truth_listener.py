#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def callback_pose(data):
    print("x=%f, y=%f, z=%f" % (data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z))

def listener():
    rospy.init_node('ground_truth_listener', anonymous=False)
    rospy.Subscriber("/ground_truth/state", Odometry, callback_pose)
    rate = rospy.Rate(1) # частота публикации сообщений
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
    listener()

