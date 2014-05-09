#!/usr/bin/env python

import os, sys

# Set arguments values
if len(sys.argv) == 1:
   print "Usage: clone-vm.py [new-vm-name]"
   exit(1)
else:
   new_vm_name = sys.argv[1]

vms_path_dir = os.getenv('HOME') + '/Documents/Virtual Machines.localized/'

vm_source_vmx = vms_home_dir + 'base-centos-64.vmwarevm/base-centos-64.vmx'

vm_dest_dir = vms_home_dir + new_vm_name + ".vmwarevm"
vm_dest_vmx = vm_dest_dir + '/' + new_vm_name + '.vmx'

if not os.path.exists(vm_dest_dir):
  os.makedirs(vm_dest_dir)

cmd = 'vmrun clone \'' + vm_source_vmx + '\' \'' + vm_dest_vmx + '\' linked -cloneName=' + new_vm_name  

print "[+] Creating new linked vm: " + new_vm_name
os.system(cmd)
