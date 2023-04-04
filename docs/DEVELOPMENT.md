```bash
cd ~
```

```bash
mkdir ~/four_ws_robot
```

```bash
cd ~/four_ws_robot
```

```bash
git clone https://github.com/5met4nka/ROS-four_ws_robot.git -b main
```

```bash
mv ROS-four_ws_robot four_ws_robot
```

```bash
git clone https://github.com/ros-planning/navigation.git -b noetic-devel
```

```bash
git clone https://github.com/5met4nka/gazebo_models_worlds_collection.git -b main
```

```bash
cd src
```

```bash
./scripts/install_pkgs.sh
```

```bash
cd ~/four_ws_robot
```

```bash
catkin build
```

```bash
cd ~
```

в случае использование терминальной оболочки `zsh`

```bash
echo "source ~/four_ws_robot/devel/setup.zsh" >> ~/.zshrc
```

или в случае терминальной оболочки `bash`

```bash
echo "source ~/four_ws_robot/devel/setup.bash" >> ~/.bashrc
```

* замечание: ROS может видеть только один ws, поэтому комментим настройку запуска других ws при помощи символа "#"
