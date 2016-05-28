import ctypes
import platform

def run(**args):
    try:
        print "[*] In lock screen module."
        
        if platform.system() == "linux" or platform.system() == "linux2":
            print ("it's Linux") #LINUX #untested
            data = "Not implemented"

        elif platform.system() == "darwin" or platform.system() == "Darwin":
            print ("it's OSX") #OSX
            data = "Not implemented"
        
        elif platform.system() == "win32" or platform.system() == "Windows":
            print ("it's Windows") # Windows
            data = ctypes.windll.user32.LockWorkStation()
        return str(data)
    except Exception as e:
        print e
        return str("e")