# основной образ
FROM osrf/ros:noetic-desktop-full

# необходимые apt-пакеты
RUN apt-get update \
    && apt-get install -y \
    sudo \
    nano

# утилита catkin
RUN apt-get update \
    && apt-get install -y \
    python3-catkin-tools

# необходимые ROS-пакеты
RUN apt-get update \
    && apt-get install -y \
    ros-$ROS_DISTRO-move-base \
    ros-$ROS_DISTRO-amcl \
    ros-$ROS_DISTRO-gmapping \
    ros-$ROS_DISTRO-map-server

# необходимые библиотеки для ROS-пакетов
RUN apt-get update \
    && apt-get install -y \
    libspnav-dev \
    libopenvdb-dev \
    libpcap-dev \
    libgeographic-dev

RUN rm -rf /var/lib/apt/lists/*

# добавляем пользователя по умолчанию
ARG USERNAME=user1122
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# копируем .bashrc
COPY bashrc /home/${USERNAME}/.bashrc

# docker image build -t lsd-maddrive-ros:noetic-devel .

# docker container run -it \
#     --name=my_container \
#     --user=user1122 \
#     --network=host \
#     --ipc=host \
#     --volume=$HOME/catkin_ws/src:/home/user1122/catkin_ws/src \
#     --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw \
#     --env=DISPLAY \
#     lsd-maddrive-ros:noetic-devel

# sudo catkin config --extend /opt/ros/noetic

# sudo ./src/four_ws_robot/scripts/build.sh
