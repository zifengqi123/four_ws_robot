клонируем и собираем необходимые пакеты

```bash
cd catkin_ws/src
```

```bash
git clone https://github.com/5met4nka/ROS-four_ws_robot.git four_ws_robot
```

```bash
git clone https://github.com/ros-planning/navigation.git -b noetic-devel
```

```bash
git clone https://github.com/5met4nka/gazebo_models_worlds_collection.git -b main
```

```bash
./four_ws_robot/scripts/install_pkgs.sh
```

```bash
cd ~/catkin_ws
```

```bash
catkin build
```

в случае использование терминальной оболочки `zsh`

```bash
echo "export CATKIN_WORKSPACE="$HOME/catkin_ws"" >> ~/.zshrc
```

или в случае терминальной оболочки `bash`

```bash
echo "export CATKIN_WORKSPACE="$HOME/catkin_ws"" >> ~/.bashrc
```