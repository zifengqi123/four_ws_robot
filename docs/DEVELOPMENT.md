клонируем необходимые пакеты

```bash
cd catkin_ws/src
```

основные пакеты

```bash
git clone https://github.com/5met4nka/ROS-four_ws_robot.git four_ws_robot
```

стек пакетов навигации

```bash
git clone https://github.com/ros-planning/navigation.git -b noetic-devel
```

hector_slam

```bash
git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git -b noetic-devel
```

slam_gmapping

```bash
git clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel
```

пакет с мирами в Gazebo

```bash
git clone https://github.com/5met4nka/gazebo_models_worlds_collection.git -b main
```

стек пакетов контроллеров для управления различными типами роботов

```bash
git clone https://github.com/ros-controls/ros_controllers -b noetic-devel
```

```bash
git clone https://github.com/ros-controls/ros_control -b noetic-devel
```

пакет с сообщениями для четырехколесного управления

```bash
git clone https://github.com/ros-drivers/four_wheel_steering_msgs.git -b master
```

пакет для обработки объектов в urdf

```bash
git clone https://github.com/ros-controls/urdf_geometry_parser.git -b kinetic-devel
```

установка оставших требуемых пакетов

```bash
./four_ws_robot/scripts/install_pkgs.sh
```

сборка пакетов

```bash
cd ~/catkin_ws
```

```bash
catkin build
```

определяем переменную `CATKIN_WORKSPACE` (она необходима для работы некоторых компонентов системы)

```bash
echo "export CATKIN_WORKSPACE="$HOME/catkin_ws"" >> ~/.zshrc
```