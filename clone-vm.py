#!/usr/bin/env python

import os
import sys

vms_home_dir = os.getenv('HOME') + '/Documents/Virtual\ Machines.localized/'
vms_home_dir_not_escaped = os.getenv('HOME') + '/Documents/Virtual Machines.localized/'

vm_source_vmx = vms_home_dir + 'base-centos-64.vmwarevm/base-centos-64.vmx'

vm_dest_dir_not_escaped = vms_home_dir_not_escaped + sys.argv[1]
vm_dest_dir = vms_home_dir + sys.argv[1]
vm_dest_vmx = vm_dest_dir + '/' + sys.argv[1] + '.vmx'

if not os.path.exists(vm_dest_dir_not_escaped):
  os.makedirs(vm_dest_dir_not_escaped)

cmd = 'vmrun clone ' + vm_source_vmx + ' ' + vm_dest_vmx + ' linked -cloneName=' + sys.argv[1]  

print cmd
os.system(cmd)
