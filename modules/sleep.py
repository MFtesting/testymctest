import time
#must be integer, no quotes
sleep_time = 60
def run(**args):
    print "[*] In sleep module."
    time.sleep(sleep_time)
return str("sleeping for %s" % sleep_time)
