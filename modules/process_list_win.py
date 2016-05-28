import os
import subprocess
import platform
try:
    import wmi
except ImportError:
    try:
        import pythoncom
    except ImportError:


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
    except ImportError:
        raise ImportError('<any message you want here>')
    except Exception as e:
        print e
        return str("e")