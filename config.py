#!/usr/bin/env python

import os, yaml

class Config(object):
    def __init__(self, debug_mode):
        # Load yaml file configuration
        if os.path.isfile( os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'):
            f = open(os.path.dirname(os.path.realpath(__file__)) + '/config.yaml')
            self.configFile = os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'
            self.configMap = yaml.safe_load(f)
          
            if debug_mode:
                print "[-] Config map: "
                print self.configMap
        
            f.close()
        else:
            print "Config file 'config.yaml' not found"
            exit(2)
    
    def getVmsPathDir(self):
        return self.configMap['vms']['path_dir']
    
    def getVmSourceVMXPath(self):
        return self.configMap['vm']['source']['vmx_path']

