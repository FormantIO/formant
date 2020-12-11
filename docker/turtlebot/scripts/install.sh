#! /bin/bash

source /opt/ros/melodic/setup.bash

apt update

# make sure we have full dependencies
apt install -y ros-melodic-desktop-full \
                ros-melodic-gmapping \
                ros-melodic-map-server \
                ros-melodic-move-base \
                ros-melodic-amcl \
                ros-melodic-dwa-local-planner \
                libgazebo9-dev \
                xvfb

mkdir -p /catkin_ws/src
pushd /catkin_ws/src
git clone https://github.com/ros-simulation/gazebo_ros_pkgs -b melodic-devel
git clone https://github.com/ROBOTIS-GIT/turtlebot3
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations
popd
pushd /catkin_ws
rosdep update
rosdep check --from-paths . --ignore-src --rosdistro melodic
catkin_make
popd