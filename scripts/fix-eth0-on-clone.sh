#!/bin/bash

# Recreate the udev/ifcfg link on a cloned virtual machine
# Delete the old udev and change the mac on the ifcfg file

# NOTE: Only works if only interface is present

# Get the new mac address
mac=$(ip link show | tail -1 | awk '{print $2}')

# Only do the switch if the new mac is not aleready in the ifcfg file
if [ $(grep -c $mac /etc/sysconfig/network-scripts/ifcfg-eth0) -eq 0 ]; then 
    # 1 - Fix the /etc/udev/rules.d/70-persistent-net.rules
    grep -v "#" /etc/udev/rules.d/70-persistent-net.rules | tail -1 > /tmp/rule$$ 
    sed 's/NAME=.*/NAME="eth0"/' /tmp/rule$$ > /tmp/rule$$.tmp
    mv /tmp/rule$$.tmp /tmp/rule$$
    mv /tmp/rule$$ /etc/udev/rules.d/70-persistent-net.rules

    # 2 Replace the new mac in the ifcfg config file
    sed 's/HWADDR.*/HWADDR='"$mac"'/' /etc/sysconfig/network-scripts/ifcfg-eth0 > /tmp/ifcfg$$

    mv /tmp/ifcfg$$  /etc/sysconfig/network-scripts/ifcfg-eth0 
fi
