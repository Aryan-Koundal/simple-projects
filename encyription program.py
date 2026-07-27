import random
import string

x = string.punctuation + string.digits + string.ascii_letters
x = list(x)
key = x.copy()
random.shuffle(key)

msg = input("Entre a msg to encrypt: ")
y = ""
for i in msg:
    idx = x.index(i)
    y += key[idx]

print (f" original message : {msg}")
print (f"encryoted message : {y}")