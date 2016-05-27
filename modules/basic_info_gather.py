import os
import platform
import time

def run(**args):
    print "[*] In basic info gather module."
    info = ""
    print platform.system()
    
    if platform.system() == "linux" or platform.system() == "linux2":
        print ("its linux") #LINUX
        info = "Linux \n"
        info += ("Timezone: %s \n" %time.tzname)
        info += str(os.environ)
    elif platform.system() == "darwin" or platform.system() == "Darwin":
        print ("it's OSX") #OSX
        info = "OSX \n"
        info += ("Timezone: %s \n" %time.tzname)
        info += str(os.environ)
    elif platform.system() == "win32" or platform.system() == "Windows":
        print ("it's Windows") # Windows
        info = "Windows \n"
        info += ("Timezone: %s \n" %time.tzname)
        info += str(os.environ)
    return str(info)



