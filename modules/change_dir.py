import os
path = "C:\\"
def run(**args):
    print "[*] In change dir module."
    chdir = os.chdir(path)
    return str(chdir)
