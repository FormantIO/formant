# Turtlebot simulator

This directory contains a container based turtlebot simulator that can be driven via keybaord input. The image is also available publically on [docker hub](https://hub.docker.com/r/formant/turtlebot).

To run turtlebot locally:

```bash
docker run -it --net --cpus 2 host -a stderr -a stdin -a stdout formant/turtlebot
```

You will see output like this if everything is working properly:

```bash
setting up xvfb display...
starting up roscore...
/catkin_ws /
launching turtlebot house...
launching turtlebot slam...
launcing turtlebot simulation...
... logging to /root/.ros/log/70600cda-b4a7-11ea-b06b-144f8ad1a849/roslaunch-abraham-fw-269.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://abraham-fw:45739/

SUMMARY
========

PARAMETERS
 * /cmd_vel_topic_name: /cmd_vel
 * /rosdistro: melodic
 * /rosversion: 1.14.6

NODES
  /
    turtlebot3_drive (turtlebot3_gazebo/turtlebot3_drive)

ROS_MASTER_URI=http://localhost:11311

process[turtlebot3_drive-1]: started with pid [406]
[ INFO] [1592844199.963400171]: TurtleBot3 Simulation Node Init
```

We use `--net=host` so you can run local tools like `rviz` or the `formant agent` against the simulation. We also limit the number of cpu's. There are a number of environment variables that can be set:

-   `HOUSE=1`: setting this uses the `house` environment for turtlebot. Default is `world`.
-   `SLAM=1`: setting this enables `slam` with `gmapping`. It will default to loading the basic `world` map.
-   `TELEOP=1`: setting this enables `turtlebot_teleop_key.launch` for commanding the turtlebot from the command line. Make sure to pass `-a stderr -a stdin -a stdout` so that input is redirected.
