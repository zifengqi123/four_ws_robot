#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

vel_msg = Twist()

def callback_teleop(data):
    global vel_msg

    if data.axes[3] == 0:
        vel_msg.linear.x = data.axes[1]
        vel_msg.linear.y = 0
        vel_msg.angular.z = data.axes[0]
    else:
        vel_msg.linear.x = data.axes[1]
        vel_msg.linear.y = data.axes[3]
        vel_msg.angular.z = 0

def joy_teleop():
    global vel_msg

    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('joy_teleop', anonymous=True)
    rospy.Subscriber('joy', Joy, callback_teleop)
    joy_teleop()
    rospy.spin()
