
from os import urandom
from base64 import b64encode
from ctypes import CDLL
import string
import hashlib

# You completed the Advanced XOR  ----   the plain text
# sNMdh  ---- the key

key=""

def get_key():
    global key

    c = urandom(1)
    if len(key)!=5:
        if c not in string.ascii_lowercase and c not in string.ascii_uppercase :
            get_key()
        else:
            key += c
            get_key()

def xor():
    get_key()
    global key
    hex_key = key.encode("hex")
    key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
    a="2a2138440b1c233d080d072b29441c1b2b6d250c052f23070d176e152b3a"
    a=bytearray.fromhex(a).decode()
    plaintext = ""
    for i in xrange(len(a)):
        plaintext += chr(ord(a[i]) ^ int(key_list[i%5], 16)) # nothing to change
    while hashlib.md5(plaintext).digest().encode("hex") != "067abbb88d2201a393ba660728f83b84": 
        key=""
        get_key()
        print(key)
        hex_key = key.encode("hex")
        key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)]
        a="2a2138440b1c233d080d072b29441c1b2b6d250c052f23070d176e152b3a"
        a=bytearray.fromhex(a).decode()
        plaintext = ""
        for i in xrange(len(a)):
            plaintext += chr(ord(a[i]) ^ int(key_list[i%5], 16)) # nothing to change
        print(plaintext)
    print(plaintext)
        
xor()
