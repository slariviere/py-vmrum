#!/usr/bin/env python
import os, sys, yaml

debug_mode = False

# Set the help menu
def getSyntax():
    return "Usage: clone-vm.py [options...] <vm_name>"

# Set arguments values
def setArguments(argv):
    opts = {}
    # Set available arguments
    valued_args = { '--username': 'username', '-u': 'username', '--password': 'password', '-p': 'password' }
    non_valued_args = { '--debug': 'debug', '--linked': 'linked', '-l': 'linked', '--full': 'full', '-f': 'full' }
    while argv:
        # If it's an option
        if argv[0][0] == '-':
            # if it's a valued argument we keep the value and cut 2 arguments form the list
            if argv[0] in valued_args:
                opts[valued_args[argv[0]]] = argv[1] 
                argv = argv[2:]
            # if it's not a valued argument we set it as true and cut 1 argument 
            elif argv[0] in non_valued_args:
                opts[non_valued_args[argv[0]]] = True 
                argv = argv[1:]
            # We don't have available definition for this argument, show the help
            else:
                print 'Invalid argument.'
                print getSyntax()
                exit(1)
        # New vm name
        elif len(argv) == 1:
           opts['name'] = argv[0]
           argv = argv[1:]
        # There is a problem with the syntax
        elif argv[0] != sys.argv[0]:
            print 'Invalid argument.'
            print getSyntax()
            exit(1)
        # This is the script name, we don't store it
        elif argv[0] == sys.argv[0]:
            argv = argv[1:]
    return opts

if len(sys.argv) == 1:
   print getSyntax() 
   exit(1)
else:
   args = setArguments(sys.argv)
   try:
       debug_mode = args['debug']
       print "[-] Args: "
       print args
   except KeyError:
       debug_mode = False

# Load yaml file configuration
if os.path.isfile('config.yaml'):
    f = open('config.yaml')
    configMap = yaml.safe_load(f)
    if debug_mode:
        print "[-] Config map: "
        print configMap
    f.close()
else:
    print "Config file 'config.yaml' not found"
    exit(2)

vm_dest_dir = configMap['vms']['path_dir'] + "/" + args['name'] + ".vmwarevm"
vm_dest_vmx = vm_dest_dir + '/' + args['name'] + '.vmx'

if not os.path.exists(vm_dest_dir):
  os.makedirs(vm_dest_dir)

cmd = "vmrun clone '" + configMap['vm']['source']['vmx_path'] + "' '" + vm_dest_vmx + "' linked -cloneName=" + args['name']  

if debug_mode:
    print "[-] vmrun command:" + cmd
else:
    print "[+] Creating new linked vm: " + args['name']
    os.system(cmd)
