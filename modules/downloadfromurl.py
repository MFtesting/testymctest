import urllib
import tempfile
import os

#download to temp for osx

def run(**args):
    url = "http://localhost:8000/meh.txt"
    print "[*] In downoadfromurl module."

    urllib.urlretrieve(url, os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
    info = os.path.getsize(os.path.join(tempfile.gettempdir() + '/'  + url.split('/')[-1]))
    return str("downloaded file of %s bytes" %info)
