# ROS-four_ws_navigation-src

## установка пакетов

<p align="center">
<img src="media/model.png">
</p>

```bash
cd
mkdir ~/four_ws_navigation
cd ~/four_ws_navigation
git clone https://github.com/5met4nka/ROS-four_ws_navigation-src.git
mv ROS-four_ws_navigation-src src
cd src
mkdir -p ~/.gazebo/models
cp -r four_ws_stage ~/.gazebo/models/four_ws_stage
rm -r four_ws_stage
cd ..
catkin_make
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
roslaunch robot_launch launch_simulation_for_navigation.launch
```

```bash
roslaunch navigation_params navigation.launch
```

<p align="center">
<img src="media/navigation.gif">
</p>

## запуск локализации

```bash
roslaunch robot_launch launch_simulation_for_localization.launch
```

```bash
roslaunch navigation_params localization.launch
```

<p align="center">
<img src="media/localization.gif">
</p>

## запуск gmapping

```bash
roslaunch robot_launch launch_simulation_for_map_creation.launch
```

```bash
roslaunch gmapping rviz_slam_gmapping_view.launch
```

<p align="center">
<img src="media/slam_gmapping.gif">
</p>

* сохранение карты в файл

```bash
cd ~/four_ws_navigation/src/navigation_params/map
```

```bash
rosrun map_server map_saver -f four_ws_map
```

# [параметры slam_gmapping](slam_gmapping_params.md)

# [параметры amcl](amcl_params.md)