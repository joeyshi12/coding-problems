# https://play.picoctf.org/practice/challenge/107

import string


def decrypt(ciphertext: str, key: str) -> str:
    text = []
    i = 0
    for c in ciphertext:
        if c.upper() in string.ascii_uppercase:
            position = string.ascii_uppercase.index(c.upper())
            offset = string.ascii_uppercase.index(key[i % len(key)])
            plain_char = string.ascii_uppercase[(position - offset) % 26]
            c = plain_char if c.isupper() else plain_char.lower()
            i += 1
        text.append(c)
    return "".join(text)


def main():
    key = "CYLAB"
    with open("cipher.txt", encoding="utf-8") as f:
        print(decrypt(f.read(), key))


if __name__ == "__main__":
    main()
