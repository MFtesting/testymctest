import os
import subprocess
import platform

def run(**args):
    try:
        print "[*] In Process List Module."
        
        if platform.system() == "linux" or platform.system() == "linux2":
            print ("it's Linux") #LINUX #untested
            data = "Not implemented"
        
        else platform.system() == "darwin" or platform.system() == "Darwin":
            print ("it's OSX") #OSX
            data = subprocess.Popen(['ps','aux'], stdout=subprocess.PIPE).stdout.readlines()

        return str(data)
    except Exception as e:
        print e
        return str("e")