import zlib
import base64
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP

encrypted = """XxfaX7nfQ48K+l0rXM3tQf3ShFcytAQ4sLe6vn8bWdreho4riaJ5Dy5PeijSKbsgWSMoeZLmihxb0YAFgCaIp11AUl4kmIiY+c+8LJonbTTembxv98GePM1SEme5/vMwGORJilw+rTdORSHzwbC56sw5NG8KosgLWwHEGEGbhii2qBkuyQrIc9ydoOKKCe0ofTRnaI2c/lb9Ot3vkEIgxCks94H6qVkAfhO34HS7nClUldn9UN040RYgtEqBgvAFzoEhDuRtfjJu1dzyzaFtRAVhcQ6HdgZMWRfpaxKQOmbhXwYyGRQfwNl/Rwgn1EJBFAhvIaEifHDlCw+hLViNYlae7IdfIb6hWtWPyFrkaNjmkbhhXclNgZe0+iPPDzsZbpHI1IckG0gVlTdlGKGz+nK5Cxyso41icC4gO7tmdXDGgF6bMt/GC1VjMVmL/rYsb8jzJblmuQBAeFNacyhjxrzIH5v60RQ1BxwfD+wLCKfyzn3vQucPak2cnwBs3yTIEShYj0ymP4idU/5Qt5qkqMDyvO4U8DmqB4KT58+o2B3c88+lUZjz7c9ygwKjp2hSNf+Dm9H3YJY2Pn6YlydyT1sYWCy06DZko7z3uae5GYGjez8hnCIFt+mpeLvEelSHeZfyV8wYyHg5Y9eA2NZNX6yNVD8IREhjXGWdbGTn41lVCqEiCetY9SKdWeL1Hp/vJN3SOo4qglbQF7P6oqqg0bofnAcphLVaHw/FOGWtW1CFEQUQdIg9bk+SJqM/s1ozJlisenrRzxv3L5LthEfLflCafK0u3n2gPa4F3ok4tx9i+r+MykRTw+OksMfVu71CAMuJdrFQLMSpyWkQ86Vc/QIXgdoCKkAYx5xr/U8gDXkZ4GvL9biEZv/fb5Wh7Br1Hu6idUgTYpEJVVnMuI13ePGeJLA54Il2S7aDyrgfhb61WQmoMRGvLP7uxCjgLwrxZNjAYJTmXszLvvgmI+lHe5o8rgQw6zSGpl9k27urV4bA0Zt+PsYiLNbEQqqxrJxKcbKqozl8XtfMXanct9pKu4vaq8fH/j9jvZ133UtcaR5iTQ0K7P4J5Qoaxz3uUhGrgplZ1jE9Nr0iyRj722dW82b4m1f/h80K7EuvwEeOfdYZl7iFL8yRi9dfopwATjKbKrWFroGCb/wvpc5ujpzDfwAeWsSU4Nve2qBDo5coVt1GI8rzHUh52TQ007JhcYABIxZGSFeeJ3bFgvqO2kUK/Pc36Au0VlNFds/j+fIuMlmFUuckBLCTpE2W9hYqmVOWBmyeZPJNzVI4gLexFbXbg8+0Eq6Pa4MxZsR3wypgC9LE/dvLbQ3oSn9x7nKMXpdq9r+xK1sjodpeYNz7t/5GpFu1teN0SFbmsoXjVEyOAn3L5Gd4Wxua7y9xOixc1H2/bbyNqJZAjEm34DDmNRTQtrqCwOEXwFGKgRGUzPYGC74wAPDDTaQEBv7Toc7rfkzgRX4ROW0SUaEPmi5tAlXe+CKVdJGtLKXUXYRHLMZ4jTzGsD89dmt2r2Fh6AUUN2e9jzzK2ULMnMhRUnDdcM74jbuDHGtXt56pFxFKJ21FQFS8JK0ZOqYa+0JjLuSzrLN9gSCu/JuTPC60LTxLsLcWZVR7cIHQE+sgDtt40/6O1YE7/8rs6qB9re28gDY1s9R5HFtjowO3ylRWqlaV9MC1OGzM4xHPxG2V+2zuq6ol8Cs="""

private_key = """-----BEGIN RSA PRIVATE KEY-----
    KEY GOES HERE
-----END RSA PRIVATE KEY-----"""


rsakey = RSA.importKey(private_key) 
rsakey = PKCS1_OAEP.new(rsakey) 


offset    = 0
decrypted = ""
encrypted = base64.b64decode(encrypted)

while offset < len(encrypted):
    decrypted += rsakey.decrypt(encrypted[offset:offset+256])
    offset += 256
    
# now we decompress to original
plaintext = zlib.decompress(decrypted)
    
print plaintext
