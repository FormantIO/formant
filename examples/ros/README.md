This directory contains `figure`, a ROS package for integrating a ROS application with Figure.

# Figure Bridge

The Figure Bridge is a ROS node that forwards ROS topics specified in the Figure Agent configuration file to the Figure Agent.

The Figure Bridge does not perform any deserialization of ROS messages; it blindly forwards messages in their serialized wire format. It does, however, register ROS message descriptions with the Figure Agent -- this allows the agent to deserialize ROS messages at runtime.

As a result, Figure has no build-time dependency on your ROS application (or vice-versa) and there should be minimal performance impact to your ROS runtime.

## Installation

```bash
cp -r ./figure <catkin_ws>/src
cd <catkin_ws>

# Manually install python requirements with pip.
# The Figure ROS package depends on protobuf 3.* and grpc 1.*.
# Unfortunately `rosdep` does not support specifying dependency versions.
pip install -r src/figure/requirements.txt

catkin_make
source devel/setup.sh
```

## Running

Before running the Figure Bridge, ensure that:

-   The Figure Agent is installed.
-   The Figure Agent configuration file exists.
-   Your ROS application is running.

```bash
rosrun figure bridge
```
