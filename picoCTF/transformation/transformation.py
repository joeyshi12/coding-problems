# https://play.picoctf.org/practice/challenge/104

def encrypt(s: str) -> str:
    if len(s) % 2:
        raise Exception("string must be of even length")
    return ''.join([chr((ord(s[i]) << 8) + ord(s[i + 1])) for i in range(0, len(s), 2)])

def decrypt(s: str) -> str:
    chars = [""] * (len(s) * 2)
    for i, c in enumerate(s):
        chars[2 * i] = chr(ord(c) >> 8)
        chars[2 * i + 1] = chr(ord(c) & 0xff)
    return "".join(chars)

def main():
    with open("enc") as f:
        print(decrypt(f.read()))

if __name__ == "__main__":
    main()
