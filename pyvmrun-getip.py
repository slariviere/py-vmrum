#!/usr/bin/env python

import os, sys, config

# Set the help menu
def getSyntax():
    return "Usage: pyvmrun-getip <vm_name>"

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
    os.system(cmd)
