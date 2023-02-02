#! /bin/bash -e

source /opt/ros/melodic/setup.bash
echo "This is the updated entrypoint script"
/usr/lib/formant/agent/formant-agent &

# for no agent output use this
# /usr/lib/formant/formant-agent > /dev/null 2>&1 &

roscore
