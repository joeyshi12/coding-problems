import base64
from Crypto.Cipher import AES

with open("7.txt", "r") as f:
    encrypted_data = base64.b64decode(f.read())

cipher = AES.new(b"YELLOW SUBMARINE", AES.MODE_ECB)
text = cipher.decrypt(encrypted_data)

print(text.decode())
