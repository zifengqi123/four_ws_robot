#!/usr/bin/env python

import rospy
import tf2_ros
import csv
import os

if __name__ == '__main__':
    rospy.init_node('tf_map_base_listener', anonymous=False)

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # определение пути к директории CATKIN_WORKSPACE
    workspace_path = os.environ['CATKIN_WORKSPACE']
    # создайте файл csv и запишите заголовки столбцов
    with open(workspace_path + '/src/four_ws_robot/slam_algorithm_comparasion/tf_map_base_listener.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('map', 'base_footprint', rospy.Time(0), rospy.Duration(1.0))

            # откройте файл csv и добавьте новые строки данных
            with open(workspace_path + '/src/four_ws_robot/slam_algorithm_comparasion/tf_map_base_listener.csv', mode='a') as file:
                writer = csv.writer(file)
                writer.writerow([trans.transform.translation.x, trans.transform.translation.y])
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            continue

        rate.sleep()