# SSH to my robot

Robots are commonly deployed behind NAT devices. These devices restrict the methods that can be used to access the robot. Notably, you cannot dial directly into the robot since it does not have a static, global address and port. The primary goal of this feature is to provide a mechanism that allows you to connect via SSH directly to your robot running the Formant agent.

The Formant agent can be installed with [port_forwarding](./install-agent.md/#port-forwarding) enabled which allows:

-   Secure file transfer using sftp
-   Secure copy using scp
-   Connect visual tools like rviz from your desktop directly to the remote robot
-   Forward any port from your robot to your local machine
-   Create on the fly VPN using SSH-VPN

It is assumed that an SSH server is already running on the robot. SSH server software (openssh-server) is installed by default in most Linux distributions.

## Setup

First make sure you have setup [`fctl`](./fctl.md). You you use the [Convenience Script](./fctl.md/#convenience-script) you can skip to [ssh](#ssh).

## Setup ssh config file

Add the following to the top of your ~/.ssh/config file

### Mac/Linux

```bash
Host *.formant
  ProxyCommand fctl port-forward $(echo %h | sed "s/\.formant$//") -r 127.0.0.1 -p %p
```

### Docker

```bash
Host *.formant
  ProxyCommand docker run -i -a stderr -a stdin -a stdout --rm -v <permanent_storage>:/root/.formant formant/fctl port-forward $(echo %h | sed "s/\.formant$//") -r 127.0.0.1 -p %p
```

Replace `<permanent_storage>` with a mount path on your local host system, and fill in your admin credentials.

This attaches STDIN, STDOUT, and STDERR to the container which is necessary for SSH ProxyCommand, as well as removing the cointainer with --rm when exiting.

### SSH

```bash
ssh <user>@<device_name>.formant
```

Replace `<device_name>` with the device name used in Formant and `<user>` is the user on the system. All standard ssh security mechanisms apply here.
