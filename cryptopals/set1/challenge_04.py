# Detect single-character XOR
# https://cryptopals.com/sets/1/challenges/4

import base64
import challenge_03


strs = []
with open("./c04_cipher.txt", encoding="utf-8") as f:
    strs = f.read().split()

s_max = ""
message = b""
best_score = -1
for s in strs:
    text, _, score = challenge_03.decrypt_single_char_xor(base64.b16decode(s, casefold=True))
    if score > best_score:
        s_max = s
        message = text
        best_score = score

print(f"ciphertext = {s_max}")
print(f"score = {best_score}")
print(f"plaintext = {message}")

