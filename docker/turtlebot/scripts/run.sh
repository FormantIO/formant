#! /bin/bash -e

export TURTLEBOT3_MODEL=waffle_pi

echo "setting up xvfb display..."
Xvfb :1 -screen 0 1600x1200x16 &>/dev/null &
export DISPLAY=:1

source /opt/ros/melodic/setup.bash

echo "starting up roscore..."
roscore &>/dev/null &

sleep 5

pushd /catkin_ws
source devel/setup.bash

if [ ! -z "$HOUSE" ]; then
    echo "launching turtlebot house..."
    roslaunch turtlebot3_gazebo turtlebot3_house.launch gui:="false" use_sim_time:="false" headless:="true" &>/dev/null &
else 
    echo "launching turtlebot world..."
    roslaunch turtlebot3_gazebo turtlebot3_world.launch gui:="false" use_sim_time:="false" headless:="true" &>/dev/null &
fi
sleep 1
if [ ! -z "$SLAM" ]; then
    echo "launching turtlebot slam..."
    roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping use_sim_time:="false" &>/dev/null &
else
    echo "loading map..."
    roslaunch turtlebot3_navigation turtlebot3_navigation.launch open_rviz:="false" use_sim_time:="false" &>/dev/null
fi
sleep 5

if [ ! -z "$TELEOP" ]; then
    echo "launching turtlebot teleop input..."
    roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch use_sim_time:="false"
else
    echo "launcing turtlebot simulation..."
    roslaunch turtlebot3_gazebo turtlebot3_simulation.launch use_sim_time:="false"
fi