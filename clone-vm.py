#!/usr/bin/env python

import os
import sys

# Set arguments values
if len(sys.argv) == 1:
   print "Usage: clone-vm.py [new-vm-name]"
   exit(1)
else:
   new_vm_name = sys.argv[1]

vms_home_dir = os.getenv('HOME') + '/Documents/Virtual\ Machines.localized/'
vms_home_dir_not_escaped = os.getenv('HOME') + '/Documents/Virtual Machines.localized/'

vm_source_vmx = vms_home_dir + 'base-centos-64.vmwarevm/base-centos-64.vmx'

vm_dest_dir_not_escaped = vms_home_dir_not_escaped + new_vm_name + ".vmwarevm"
vm_dest_dir = vms_home_dir + new_vm_name
vm_dest_vmx = vm_dest_dir + '/' + new_vm_name + '.vmx'

if not os.path.exists(vm_dest_dir_not_escaped):
  os.makedirs(vm_dest_dir_not_escaped)

cmd = 'vmrun clone ' + vm_source_vmx + ' ' + vm_dest_vmx + ' linked -cloneName=' + new_vm_name  

print "[+] Creating new linked vm"
os.system(cmd)
