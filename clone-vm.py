#!/usr/bin/env python

import os, sys, yaml

# Set arguments values
if len(sys.argv) == 1:
   print "Usage: clone-vm.py [new-vm-name]"
   exit(1)
else:
   new_vm_name = sys.argv[1]

if os.path.isfile('config.yaml'):
    f = open('config.yaml')
    configMap = yaml.safe_load(f)
    f.close()
else:
    print "Config file 'config.yaml' not fourd"
    exit(2)

vm_dest_dir = configMap['vms']['path_dir'] + "/" + new_vm_name + ".vmwarevm"
vm_dest_vmx = vm_dest_dir + '/' + new_vm_name + '.vmx'

if not os.path.exists(vm_dest_dir):
  os.makedirs(vm_dest_dir)

cmd = 'vmrun clone \'' + configMap['vm']['source']['vmx_path'] + '\' \'' + vm_dest_vmx + '\' linked -cloneName=' + new_vm_name  

print "[+] Creating new linked vm: " + new_vm_name
os.system(cmd)
