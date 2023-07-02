#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# создаем объект Twist для хранения сообщений команды движения
vel_msg = Twist()

# флаг, указывающий, было ли уже опубликовано нулевое сообщение
zero_command_published = False

def callback_teleop(data):
    global vel_msg

    # обновляем значения линейной и угловой скорости из данных джойстика
    vel_msg.linear.x = data.axes[1]
    vel_msg.angular.z = data.axes[0]

def joy_teleop():
    global vel_msg, zero_command_published

    # создаем паблишер для публикации сообщений команды движения в топик "cmd_vel"
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        # публикуем только ненулевые команды движения
        if vel_msg.linear.x != 0 or vel_msg.angular.z != 0:
            zero_command_published = False
            pub.publish(vel_msg)
        # публикуем нулевую команду только один раз
        elif vel_msg.linear.x == 0 and vel_msg.angular.z == 0 and not zero_command_published:
            zero_command_published = True
            pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    # инициализируем узел ROS с именем 'joy_teleop'
    rospy.init_node('joy_teleop', anonymous=True)
    # подписываемся на топик 'joy' и указываем функцию обратного вызова 'callback_teleop'
    rospy.Subscriber('joy', Joy, callback_teleop)
    # вызываем функцию 'joy_teleop', которая содержит основной цикл программы
    joy_teleop()
    # запускаем основной цикл ROS
    rospy.spin()
