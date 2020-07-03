For general information on installing the Formant agent, see [agent debian installation](./agent-debian-install.md).

### Agent installation FAQ

#### Can I download the Formant agent and sidecar debian packages directly?

Yes. [See here for debian packages](https://formant.jfrog.io/ui/packages?name=formant&type=packages).

Install using
`dpkg -i <formant-package>.deb`

#### Can I install the Formant agent on Windows or MacOS?

We support agent installation via docker container for non-Linux systems. [See agent docker install](./agent-docker-install.md).

#### What environment variables can I add to /var/lib/formant/.bashrc?

Here is a list of optional environment variables that affect the behavior of the Formant agent:

```
	// ROS-specific:

	// The path to the root of the catkin workspace. The Formant agent uses this to find custom ROS message definitions
	CATKIN_WS

	// If the ROS setup files are not in <catkin_ws>/devel/setup.bash, the custom location of ROS setup script
	SOURCE_SCRIPT

	// The file location of the Python interpreter used by the tf2 bridge
	FORMANT_AGENT_PYTHON_PATH

	// The file location of the Python3 interpreter used by the ROS bridge
	FORMANT_AGENT_PYTHON3_PATH

	// The address of the ROS master to which the ROS Bridge connects
	ROS_MASTER_URI

	// The file localtion of the unix socket used for the ROS bridge
	FORMANT_ROS_AGENT_GRPC_UNIX_SOCKET

	// Enables replacement of timestamps on ROS messages with the current time
	FORMANT_OVERRIDE_TIMESTAMP

	// ROS-agnostic:

	// The IP address where the Formant Agent will start it's server
	FORMANT_AGENT_IP

	// The Unix Socket where the Formant Agent will start it's server
	FORMANT_AGENT_GRPC_UNIX_SOCKET

	// The port where the Formant Agent will expose the gRPC interface
	FORMANT_AGENT_GRPC_PORT

	// The port where the Formant Agent will expose the HTTP interface
	FORMANT_AGENT_HTTP_PORT

	// Enables the local port forwarding feature
	FORMANT_PORT_FORWARDING
```

#### How can I make the "formant" user use a different python than the system level python?

Export `FORMANT_AGENT_PYTHON_PATH` and `FORMANT_AGENT_PYTHON3_PATH` to the desired values in `/var/lib/formant/.bashrc` to specify the pythons the `formant` user will use. These values default to `python` and `python3`.

### Agent setup troubleshooting

#### The Formant agent ROS bridge is not running

Most parts of the formant agent ROS bridge are `python3` processes. Try running `import rospy` in a `python3` shell. If this import errors, you may have to install `python3-roskpg-modules`:

-   `apt install python3-rospkg-modules`

#### ImportError: cannot import name Gst, introspection typelib not found

Some systems will not have a video streaming dependency installed. To fix, you can install the following:

-   `apt install gir1.2-gst-rtsp-server-1.0`

#### /usr/sbin/policy-rc.d returned 101, not running 'enable formant-agent.service'

The system's policy-rd.d may be set up to disallow enabling services. Edit `/usr/sbin/policy-rc.d` to exit 0 instead of 101.

### Didn't find what you were looking for?

Contact us directly:

-   support@formant.io
