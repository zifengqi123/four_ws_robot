#!/bin/bash

export ZSH="$HOME/.oh-my-zsh"

source $ZSH/oh-my-zsh.sh

# aliases
alias ls='ls -a'

source /opt/ros/noetic/setup.zsh
source ~/catkin_ws/devel/setup.zsh

export CATKIN_WORKSPACE="$HOME/catkin_ws"
export GAZEBO_MODEL_PATH=$(rospack find maddrive_worlds)/models