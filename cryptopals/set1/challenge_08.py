import base64
from Crypto.Cipher import AES

with open("8.txt", "r") as f:
    while True:
        line = f.readline().strip().upper()
        if len(line) == 0:
            break
        line_bytes = base64.b16decode(line)
        print(len(line_bytes))
