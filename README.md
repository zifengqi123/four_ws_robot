# ROS-four_ws_navigation-src

## установка пакетов

```bash
cd
```

```bash
mkdir ~/four_ws_navigation
```

```bash
cd ~/four_ws_navigation
```

```bash
git clone https://github.com/5met4nka/ROS-four_ws_navigation-src.git
```

```bash
mv ROS-four_ws_navigation-src src
```

```bash
cd src
```

```bash
cp -r four_ws_stage /home/USER_NAME/.gazebo/models
```

```bash
rm -r four_ws_stage
```

```bash
cd ..
```

```bash
catkin_make
```

```bash
cd
```

в случае использование zsh  

```bash
echo "source ~/four_ws_navigation/devel/setup.zsh" >> ~/.zshrc
```

или в случает bash  

```bash
echo "source ~/four_ws_navigation/devel/setup.bash" >> ~/.bashrc
```

* замечание: ROS может видеть только один ws, поэтому комментим настройку запуска других ws при помощи символа "#"

## запуск навигации

```bash
roslaunch robot_launch launch_navigation_simulation.launch
```

```bash
roslaunch navigation_params navigation.launch
```

## запуск gmapping

```bash
roslaunch robot_launch launch_simulation_for_map_creation.launch
```

```bash
rosrun gmapping slam_gmapping scan:=/front/scan
```

```bash
rosrun map_server map_saver -f four_ws_map
```
