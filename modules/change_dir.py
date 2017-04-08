import os
path = "C:\"
def run(**args):
    print "[*] In getcwd module."
    chdir = os.chdir(path)
    return str(chdir)
