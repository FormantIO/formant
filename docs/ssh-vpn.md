# Setting up a VPN tunnel over SSH with Formant

This guide will demonstrate how to setup a VPN tunnel (tun0) over SSH using Formant's port-forwarding capabilities over our peer-to-peer communication channel. Before starting with this guide, make sure you have setup a device with the [agent](./agent-debian-install.sh), and have setup on your client machine [fctl](./fctl.md) and configured [ssh](./ssh.md). This guide is based on the existing [SSH VPN](https://help.ubuntu.com/community/SSH_VPN) community guide.

## Device Configuration (Run all of these on the machine with the agent installed)

Using any editor, open /etc/ssh/sshd_config and change the "PermitRootLogin" line and add the "PermitTunnel" line:

```
PermitRootLogin without-password
PermitTunnel yes
```

Allow NAT. These commands will enable NAT without the need to reboot (NAT will be persistent). This may already be enabled on your system.

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

To set as default, using any editor, open /etc/sysctl.conf and add:

```
# Needed to add for forwarding
net.ipv4.ip_forward = 1
```

Create the `tun0` network interface by adding a network interface. Create the file `/etc/network/interfaces.d/tun0` and add:

```
 iface tun0 inet static
        pre-up sleep 5
        address 10.0.0.100
        pointopoint 10.0.0.200
        netmask 255.255.255.0
        up arp -sD 10.0.0.200 eth0 pub
```

The Formant agent runs with it's own user and group (`formant:formant`) that, by default, has very limited permissions. To enable the agent to create a `tun` interface we need to add it to the device's sudoers group:

```bash
sudo usermod -aG sudo formant
sudo systemctl restart formant-agent
```

Note: the `formant` user has no shell or login by design.

## Client Configuration

Generate a ssh key, here we call it `formant-vpn`:

```bash
ssh-keygen -f formant-vpn -b 4096
```

Put the private key `formant-vpn` in `/root/.ssh` and set permissions:

```
# create this directory if it doesn't exist
sudo mkdir -p /root/.ssh
sudo cp formant-vpn /root/.ssh/formant-vpn
sudo chown root:root /root/.ssh/formant-vpn
sudo chmod 400 /root/.ssh/formant-vpn
```

Copy the public key `formant-vpn.pub` onto the device. Once there add it to the authorized keys (Run this ON the device):

```bash
# if the root ssh folder doesn't exist, create it
sudo mkdir -p /root/.ssh
sudo bash -c "cat formant-vpn.pub >> /root/.ssh/authorized_keys"
```

We need to setup a seperate auth location for `fctl` tokens:

```bash
sudo fctl init --config-directory /root/.formant
```

Setup the `root` user `ssh_config` by adding this snippet to `/root/.ssh/config`:

```
Host *.formant
  ProxyCommand fctl port-forward $(echo %h | sed "s/\.formant$//") -r 127.0.0.1 -p %p --config-directory /root/.formant
```

## SSH Commands on client

Open a new terminal and run this command to stand up the tunnel

```bash
sudo ssh -i /root/.ssh/formant-vpn -Cf -w 0:0 nano.001.formant 'ifdown tun0; ifup tun0'
```

This is running ssh with tunneling (`-w`) as well as using compression on the channel (`-C`) and forking it to the background (`-f`). Additionally, it tells our device to run `ifdown tun0; ifup tun0`

Note: You may see `RTNETLINK answers: Cannot assign requested address` which can happen if you rerun this command (the device may already have it's addresses setup.)

Next we need to setup `tun0` on our client machine:

```bash
sudo ip link set tun0 up
sudo ip addr add 10.0.0.200/32 peer 10.0.0.100 dev tun0
sudo ip route add 10.0.0.0/24 via 10.0.0.200
```

Which configures `tun0` on the client machine and routes traffic on 10.0.0.0/24 back to our device.

You can check the tunnel is established with:

```bash
ifconfig
```

and you should see something like the following on the client machine:

```
tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.0.200  netmask 255.255.255.255  destination 10.0.0.100
        inet6 fe80::45f3:9856:2ef0:9b50  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 4  bytes 192 (192.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1  bytes 48 (48.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

and on the device:

```
tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.0.100  netmask 255.255.255.255  destination 10.0.0.200
        inet6 fe80::1fc:7f5f:6948:9e8d  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 80  bytes 12604 (12.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 90  bytes 13785 (13.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Try pinging the device from your client machine:

```bash
ping 10.0.0.100
```

To tear down the connection get the pid of the ssh command:

```bash
ps aux | grep ssh
```

Once you have the pid you can kill it:

```bash
sudo kill -9 $pid
```

The following is a [short script](./client-ssh.sh) to automate the client process. It accepts one input parameter which is the name of the device you are connecting to:

```bash
#! /bin/bash -e

device=$1


echo "setting up ssh tunnel..."

sudo ssh -i /root/.ssh/formant-vpn -Cf -w 0:0 $device.formant 'ifdown tun0; ifup tun0'

echo "ssh tunnel setup."

sudo ip link set tun0 up
sudo ip addr add 10.0.0.200/32 peer 10.0.0.100 dev tun0
sudo ip route add 10.0.0.0/24 via 10.0.0.200

echo "tun0 configured"

sleep infinity
```

Exiting the script will also tear down the ssh tunnel.

If you plan on keeping long running ssh tunnels to your devices you may want to also set the following in your ssh config:

```
Host *
  ServerAliveInterval 120
  ServerAliveCountMax 10
```

The `ServerAliveInterval` will send a ping every 120 seconds if there is no activity on the tunnel. The `ServerAliveCountMax` defines how many consecutive pings are sent before disconnecting.
