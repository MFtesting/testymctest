import os
import subprocess
import wmi
import pythoncom
import platform

def run(**args):
    try:
        print "[*] In Process List Module."
        
        print ("it's Windows") # Windows
        pythoncom.CoInitialize()
        data = ""
        w = wmi.WMI ()
        data += "PID \tPPID \tNAME \n"
        for process in w.Win32_Process ():
            data += str(process.ProcessId) + "\t" + str(process.ParentProcessId) +"\t" + str(process.Name) +"\n"
        return str(data)
    except Exception as e:
        print e
        return str("e")
        pass