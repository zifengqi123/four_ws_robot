#!/usr/bin/env python

import rospy
import os

def main():
    # Инициализируем узел ROS
    rospy.init_node('map_saver_node')

    # Получаем путь к рабочему пространству из переменных среды
    workspace_path = os.environ['CATKIN_WORKSPACE']

    # Формируем путь к папке "maps" внутри пакета "four_ws_robot_software"
    maps_path = os.path.join(workspace_path, 'src/four_ws_robot/four_ws_robot_software/maps')

    # Получаем значение параметра "map_name" из сервера параметров ROS
    map_name = rospy.get_param('/map_name', 'my_map')

    # Запускаем команду сохранения карты, используя путь к папке "maps" и значение параметра "map_name"
    command = 'rosrun map_server map_saver -f {}'.format(os.path.join(maps_path, map_name))
    os.system(command)

if __name__ == '__main__':
    main()