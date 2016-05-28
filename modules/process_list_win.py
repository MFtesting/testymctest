import os
import subprocess
import platform
try:
    import wmi
except ImportError:
    raise
    try:
        import pythoncom
    except ImportError:
        raise


        def run(**args):
            try:
                print "[*] In Process List Module."
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
run()