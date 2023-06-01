# ROS-four_ws_robot-src

<p align="center">
<img src="docs/model.gif">
</p>

> ### инструкция по началу работы находится [здесь](docs/DEVELOPMENT.md)

## запуск навигации

```bash
roslaunch four_ws_robot_software sim_start.launch mode:=navigation
```

<p align="center">
<img src="docs/navigation.gif">
</p>

## запуск локализации

```bash
roslaunch four_ws_robot_software sim_start.launch mode:=localization
```

<p align="center">
<img src="docs/localization.gif">
</p>

## запуск SLAM

```bash
roslaunch four_ws_robot_software sim_start.launch mode:=mapping
```

<p align="center">
<img src="docs/slam_gmapping.gif">
</p>

* сохранение карты в файл

```bash
roslaunch four_ws_robot_software map_saver.launch
```

# [описание параметров slam_gmapping](docs/slam_gmapping_params.md)

> ## [настройка slam_gmapping в этом проекте](four_ws_robot_software/config/slam_gmapping_params/slam_gmapping_params_test.yaml)

# [описание параметров hector_mapping](docs/hector_mapping_params.md)

> ## [настройка hector_mapping в этом проекте](four_ws_robot_software/config/hector_mapping_params/hector_mapping_params_test.yaml)

# [описание параметров amcl](docs/amcl_params.md)

> ## [настройка amcl в этом проекте](four_ws_robot_software/config/amcl_params/amcl_params_test.yaml)

# [описание параметров movebase](docs/movebase_params.md)

> ## [настройка movebase в этом проекте](four_ws_robot_software/config/movebase_params/movebase_params_test.yaml)