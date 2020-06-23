# Agent debian installation

## Supported Systems

We currently support `xenial`, `bionic`, `stretch`, `jessie`, and `buster` on `amd64`, `arm64`, and `arm`.

## Repo Setup

To get setup with Formant's debian repository you will need to add our repo to the machines source list:

```bash
sudo echo "deb [arch=<arch>] https://repo.formant.io/formant/debian $(lsb_release -cs) main" >>/etc/apt/sources.list
```

Replace `<arch>` with your architecture (`amd64`, `arm64`, or `arm`)

Next add Formants gpg key:

```bash
sudo apt-key adv --fetch-keys https://keys.formant.io/formant.pub.gpg
```

Verify that you now have the key with the fingerprint ,`6EDB 1254 D11E D6D4 E2FD D26A 9983 EFEB D4D9 CD6A` by searching for the last 8 characters of the fingerprint.

```bash
sudo apt-key fingerprint D4D9CD6A

pub   rsa4096 2019-08-13 [SCEA]
      6EDB 1254 D11E D6D4 E2FD  D26A 9983 EFEB D4D9 CD6A
uid           [ unknown] Formant (Formant signing key) <support+dev@formant.io>
```

## Installation

To install the agent you can simply run the following:

```bash
sudo apt update
sudo apt install formant-agent
```

However, before running these steps please see all the configuration options below. We also support [OTA](#ota) of the agent.

## Agent installation configuration

Before installing the agent, there are several configuration options that can be set via `debconf`.

### Provisioning token

If you are using a provisioning token for the installation it can be set with:

```bash
echo formant-agent formant-agent/token password "<token>" | sudo debconf-set-selections
```

Replace `<token>` with your token

### Provision with Formant credentials

Using a token is preferred over using Formant Credentials for security reasons, however we do allow provisioning of agents with credentials. You can do this via:

```bash
echo formant-agent formant-agent/email string "<email>" | sudo debconf-set-selections
echo formant-agent formant-agent/password password "<password>" | sudo debconf-set-selections
```

Replace `<email>` and `<password>` with your credentials.

### ROS master URI

If you are on ROS you will need to setup the agent with the ROS Master URI:

```bash
echo formant-agent formant-agent/ros_master_uri string "<ros_master_uri>" | sudo debconf-set-selections
```

Replace `<ros_master_uri>` with the correct value.

### ROS catkin workspace

The agent supports parsing of custom ROS message types, however we need to source the `setup.bash` file located within that workspace.

```bash
echo formant-agent formant-agent/catkin_ws string "<catkin_ws>" | sudo debconf-set-selections
```

Replace `<catkin_ws>` with the absolute path to your catkin workspace.

**Note**: The agent assumes the `setup.bash` file is in `/<catkin_ws>/devel/setup.bash`. If your setup file is in a different location use [source_script](#source-script).

### Source Script

To support custom locations of catkin workspace setup files, the agent allows a custom location for a script to source.

```bash
echo formant-agent formant-agent/source_script string "<source_script>" | sudo debconf-set-selections
```

Replace `<source_script>` with the absolute path to the script to source.

### System resources

The agent installation supports setting parameters for system resource usage for `cpu_quota` and `memory_limit`

Set these with:

```bash
echo formant-agent formant-agent/cpu_quota string "<cpu_quota>" | sudo debconf-set-selections
echo formant-agent formant-agent/memory_limit string "<memory_limit>" | sudo debconf-set-selections
```

`cpu_quota`: The value of the CPUQuota parameter, which is expressed in percentage, specifies how much CPU time the unit gets at maximum, relative to the total CPU time available on one CPU.

`memory_limit`: Use suffixes K, M, G, or T to identify Kilobyte, Megabyte, Gigabyte, or Terabyte as the unit of measurement.

### Service enable

You can install the agent in a disabled state with the `service_enable` parameter. This is `true` by default.

```bash
echo formant-agent formant-agent/service_enable boolean "<enable>" | sudo debconf-set-selections
```

`<enable>` can be `true` or `false`.

### Port forwarding

The agent supports port forwarding to power remote SSH, SCP, and other advanced networking tools. This can be controlled via configuration as well, however for security purposes we support disabling this at install time. This is `true` by default.

```bash
echo formant-agent formant-agent/port_forwarding boolean "<enable>" | sudo debconf-set-selections
```

`<enable>` can be `true` or `false`.

## OTA

Formant also supports over-the-air updates of the agent via a separate debian sidecar package called `formant-sidecar`.

To enable OTA all you need to do is install this additional package:

```bash
sudo apt update
sudo apt install formant-sidecar
```

By default the agent creates a `formant` user and group on the host system with no sudo permissions. However, to perform upgrades the `formant-sidecar` adds restricted sudo capabilities to the `formant` user. When the package is installed you can see them at `/etc/sudoers.d/formant`

The restricted permissions are:

```
formant ALL=(ALL) NOPASSWD:/usr/bin/apt update, /usr/bin/apt install --upgrade-only -y formant-agent, /usr/bin/apt install --upgrade-only -y formant-agent=[0-9]*.[0-9]*.[0-9]*, /usr/bin/apt remove formant-agent, /usr/bin/apt remove --purge formant-agent
```
