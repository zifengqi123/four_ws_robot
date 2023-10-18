# основной образ
FROM osrf/ros:noetic-desktop-full

# необходимые apt-пакеты
RUN apt-get update \
    && apt-get install -y \
    sudo \
    nano \
    && rm -rf /var/lib/apt/lists/*

# утилита catkin
RUN apt-get update \
    && apt-get install -y \
    python3-catkin-tools \
    && rm -rf /var/lib/apt/lists/*

# необходимые ROS-пакеты
RUN apt-get update \
    && apt-get install -y \
    ros-$ROS_DISTRO-move-base \
    ros-$ROS_DISTRO-amcl \
    ros-$ROS_DISTRO-gmapping \
    ros-$ROS_DISTRO-map-server \
    && rm -rf /var/lib/apt/lists/*

# необходимые библиотеки для ROS-пакетов
RUN apt-get update \
    && apt-get install -y \
    libspnav-dev \
    libopenvdb-dev \
    libpcap-dev \
    libgeographic-dev \
    && rm -rf /var/lib/apt/lists/*

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
