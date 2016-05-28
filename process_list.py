import os
import subprocess

def run(**args):
    print "[*] In Process List OSX module."
    data = subprocess.Popen(['ps','aux'], stdout=subprocess.PIPE).stdout.readlines()
    return str(data)