import os
import platform

def run(**args):
    print "[*] In basic info gather module."
    info = ""
    print platform.system()
    
    if platform.system() == "linux" or platform.system() == "linux2":
        print ("its linux") #LINUX
        info = "Linux \n"
        info += os.environ
    elif platform.system() == "darwin" or platform.system() == "Darwin":
        print ("it's OSX") #OSX
        info = "OSX \n"
        info += os.environ
    elif platform.system() == "win32":
        print ("it's Windows") # Windows
        info = "Windows \n"
        info += os.environ
    return str(info)



