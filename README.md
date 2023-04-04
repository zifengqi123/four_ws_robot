# ROS-four_ws_robot-src

<p align="center">
<img src="docs/model.gif">
</p>

> ### инструкция по началу работы находится [здесь](docs/DEVELOPMENT.md)

## запуск навигации

```bash
roslaunch robot_launch launch_simulation_for_navigation.launch
```

```bash
roslaunch navigation_params navigation.launch
```

<p align="center">
<img src="docs/navigation.gif">
</p>

## запуск локализации

```bash
roslaunch robot_launch launch_simulation_for_localization.launch
```

```bash
roslaunch navigation_params localization.launch
```

<p align="center">
<img src="docs/localization.gif">
</p>

## запуск gmapping

```bash
roslaunch robot_launch launch_simulation_for_map_creation.launch
```

```bash
roslaunch gmapping rviz_slam_gmapping_view.launch
```

<p align="center">
<img src="docs/slam_gmapping.gif">
</p>

* сохранение карты в файл

```bash
cd ~/four_ws_robot/src/four_ws_robot/navigation_params/map
```

```bash
rosrun map_server map_saver -f four_ws_map
```

# [описание параметров slam_gmapping](docs/slam_gmapping_params.md)

> ## [настройка slam_gmapping в этом проекте](slam_gmapping_params/gmapping/config/gmapping_params_test.yaml)

# [описание параметров amcl](docs/amcl_params.md)

> ## [настройка amcl в этом проекте](navigation_params/config/amcl/amcl_params_test.yaml)

# [описание параметров movebase](docs/movebase_params.md)

> ## [настройка movebase в этом проекте](navigation_params/config/movebase/movebase_params_test.yaml)
