#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('tf_map_base_listener', anonymous=False)

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('map', 'base_footprint', rospy.Time(0), rospy.Duration(1.0))
            print("x=%f, y=%f, z=%f" % (trans.transform.translation.x, trans.transform.translation.y, trans.transform.translation.z))
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            continue

        rate.sleep()
