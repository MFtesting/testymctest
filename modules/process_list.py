import os
import subprocess
import wmi
import pythoncom
import platform

def run(**args):
    try:
        print "[*] In Process List Module."
        
        if platform.system() == "linux" or platform.system() == "linux2":
            print ("it's Linux") #LINUX #untested
            data = "Not implemented"
        
        elif platform.system() == "darwin" or platform.system() == "Darwin":
            print ("it's OSX") #OSX
            data = subprocess.Popen(['ps','aux'], stdout=subprocess.PIPE).stdout.readlines()

        elif platform.system() == "win32" or platform.system() == "Windows":
            print ("it's Windows") # Windows
            pythoncom.CoInitialize()
            data = ""
            w = wmi.WMI ()
            data += "PID \tPPID \tNAME \n"
            for process in w.Win32_Process ():
                data += str(process.ProcessId) + "\t" + str(process.ParentProcessId) +"\t" + str(process.Name) +"\n"
            print str(data)
        return str(data)
    except Exception as e:
        print e
        return str("e")