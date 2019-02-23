This directory contains `formant`, a ROS package for integrating a ROS application with formant.

# Formant Bridge

The Formant Bridge is a ROS node that forwards ROS topics specified in the Formant Agent configuration file to the Formant Agent.

The Formant Bridge does not perform any deserialization of ROS messages; it blindly forwards messages in their serialized wire format. It does, however, register ROS message descriptions with the Formant Agent -- this allows the agent to deserialize ROS messages at runtime.

As a result, Formant has no build-time dependency on your ROS application (or vice-versa) and there should be minimal performance impact to your ROS runtime.

## Installation

```bash
cp -r ./formant <catkin_ws>/src
cd <catkin_ws>

# Manually install python requirements with pip.
# The Formant ROS package depends on protobuf 3.* and grpc 1.*.
# Unfortunately `rosdep` does not support specifying dependency versions.
pip install -r src/formant/requirements.txt

catkin_make
source devel/setup.sh
```

## Running

Before running the Formant Bridge, ensure that:

-   The Formant Agent is installed.
-   The Formant Agent configuration file exists.
-   Your ROS application is running.

```bash
rosrun formant bridge
```
