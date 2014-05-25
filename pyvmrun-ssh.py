#!/usr/bin/env python

import os, sys, config

# Set the help menu
def getSyntax():
    return "Usage: pyvmrun-ssh <vm_name>"

# Parsing arguments
if len(sys.argv) == 1:
    print getSyntax() 
    exit(1)
else:
    conf = config.Config()
    vm_start_dest = conf.getVmsPathDir() + "/" + sys.argv[1] +  ".vmwarevm/" +  sys.argv[1] + ".vmx"
    if not os.path.exists(vm_start_dest):
        print "Virtual machine not found."
        exit(1)
    cmd = "vmrun getGuestIPAddress '" + vm_start_dest + "'"
    response = os.popen(cmd)
    while 1:
        line = response.readline()
        # Check if the VM is started, and stats it if not
        if "Error: The virtual machine is not powered on" in line:
            cmd = "pyvmrun-start " + sys.argv[1]
            os.system(cmd)
        if line != "":
            ip=line
        if not line: break

    #If the username is not as arguement, we use root
    if len(sys.argv) >= 3:
        username = sys.argv[2]
    else:
        username = "root"

    cmd = "ssh " + username + "@" + ip
    os.system(cmd)
