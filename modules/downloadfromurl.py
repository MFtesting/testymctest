import urllib
import tempfile
import os
import platform

#download to temp for osx

def run(**args):
    url = "http://localhost:8000/meh.txt"
    print "[*] In downoadfromurl module."
    
    if platform.system() == "linux" or platform.system() == "linux2":
        print ("its linux") #LINUX
    elif platform.system() == "darwin":
        print ("its OSX") #OSX
        urllib.urlretrieve(url, os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
        info = os.path.getsize(os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
   elif platform.system() == "win32":
        print ("it's Windows") # Windows
        urllib.urlretrieve(self.url, os.path.join(os.getenv('TEMP') + '\\'  + self.url.split('/')[-1]))
        info = os.path.getsize(os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
    return str("downloaded file of %s bytes" %info)
