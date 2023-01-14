# ROS-four_ws_navigation-src

create four_ws_navigation workspace  

place four_ws_stage folder into /.gazebo/models directory  

## запуск навигации

```bash
$ roslaunch robot_launch launch_navigation_simulation.launch
```

```bash
$ roslaunch navigation_params navigation.launch
```

## запуск gmapping

```bash
$ roslaunch robot_launch launch_simulation_for_map_creation.launch
```

```bash
$ rosrun gmapping slam_gmapping scan:=/front/scan
```

```bash
$ rosrun map_server map_saver -f four_ws_map
```
