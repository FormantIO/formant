#! /bin/bash -e

source /opt/ros/melodic/setup.bash

/usr/lib/formant/formant-agent &

# for no agent output use this
# /usr/lib/formant/formant-agent > /dev/null 2>&1 &

roscore