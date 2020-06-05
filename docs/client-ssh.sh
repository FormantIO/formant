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
