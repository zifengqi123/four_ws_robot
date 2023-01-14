# ROS-four_ws_navigation-src

## перед тем как приступать к запуску выполняем последовательность действий

```bash
cd
```

```bash
mkdir -p ~/four_ws_navigation/src
```

```bash
cd ~/four_ws_navigation/src
```

```bash
git clone https://github.com/5met4nka/ROS-four_ws_navigation-src.git
```

```bash
cp -r four_ws_stage /home/USER_NAME/.gazebo/models
```

```bash
rm -r four_ws_stage
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

place four_ws_stage folder into /.gazebo/models directory  

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
