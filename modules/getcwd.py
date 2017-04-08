import os

def run(**args):
    print "[*] In getcwd module."
    gcwd = os.getcwd

    return str(gcwd)
