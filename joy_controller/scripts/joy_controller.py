#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

vel_msg = Twist()

def callback_controller(data):
    global vel_msg

    if data.axes[3] == 0:
        vel_msg.linear.x = data.axes[1]
        vel_msg.linear.y = 0
        vel_msg.angular.z = data.axes[0]
    else:
        vel_msg.linear.x = data.axes[1]
        vel_msg.linear.y = data.axes[3]
        vel_msg.angular.z = 0

def joy_controller():
    global vel_msg

    pub = rospy.Publisher('four_wheel_steering_controller/cmd_vel', Twist, queue_size = 10)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('joy_controller', anonymous=True)
    rospy.Subscriber("joy0", Joy, callback_controller)
    joy_controller()
    rospy.spin()
