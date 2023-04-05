# ROS-four_ws_robot-src

<p align="center">
<img src="docs/model.gif">
</p>

> ### инструкция по началу работы находится [здесь](docs/DEVELOPMENT.md)

## запуск навигации

```bash
roslaunch four_ws_robot_software simulation_for_navigation.launch
```

```bash
roslaunch four_ws_robot_software navigation.launch
```

<p align="center">
<img src="docs/navigation.gif">
</p>

## запуск локализации

```bash
roslaunch four_ws_robot_software simulation_for_localization.launch
```

```bash
roslaunch four_ws_robot_software localization.launch
```

<p align="center">
<img src="docs/localization.gif">
</p>

## запуск картографирования

```bash
roslaunch four_ws_robot_software simulation_for_map_creation.launch
```

```bash
roslaunch four_ws_robot_software mapping.launch
```

<p align="center">
<img src="docs/slam_gmapping.gif">
</p>

* сохранение карты в файл

```bash
cd ~/four_ws_robot/src/four_ws_robot/four_ws_robot_software/maps
```

```bash
rosrun map_server map_saver -f four_ws_map
```

# [описание параметров slam_gmapping](docs/slam_gmapping_params.md)

> ## [настройка slam_gmapping в этом проекте](four_ws_robot_software/config/slam_gmapping_params/slam_gmapping_params_test.yaml)

# [описание параметров amcl](docs/amcl_params.md)

> ## [настройка amcl в этом проекте](four_ws_robot_software/config/amcl_params/amcl_params_test.yaml)

# [описание параметров movebase](docs/movebase_params.md)

> ## [настройка movebase в этом проекте](four_ws_robot_software/config/movebase_params/movebase_params_test.yaml)