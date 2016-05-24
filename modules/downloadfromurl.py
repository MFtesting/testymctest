import urllib2
import json
import os

#download to temp

def run(**args):
    url = "http://localhost:8000/meh.txt"
    print "[*] In downoadfromurl module."
    meh = urllib.urlretrieve(url, os.path.join(os.getenv('TEMP') + '\\'  + url.split('/')[-1]))
    print meh

    return ("something")

