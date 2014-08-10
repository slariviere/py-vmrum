#!/bin/bash

# Prepare the line to append in the /etc/issue file
echo -n "IPs: " > /tmp/ip$$
ip a | grep inet | grep -v inet6 | awk '{print $2}' | xargs echo >> /tmp/ip$$

if [ $(grep -c IPs /etc/issue) -eq 1 ]; then
  # There is already an IPs line, the line will be updated
  ipline=$(cat /tmp/ip$$ | sed 's/\//\\\//g')
  sed 's/IPs.*/'"$ipline"'/' /etc/issue > /tmp/issue$$
  mv /tmp/issue$$ /etc/issue
else
  # Add the line at the end
  cat /tmp/ip$$ >> /etc/issue
fi

rm /tmp/ip$$
