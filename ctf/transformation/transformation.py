# https://play.picoctf.org/practice/challenge/104

def encrypt(s: str) -> str:
    if not s:
        return s
    if len(s) % 2:
        raise Exception("string must be of even length")
    return ''.join([chr((ord(s[i]) << 8) + ord(s[i + 1])) for i in range(0, len(s), 2)])

def decrypt(s: str) -> str:
    if not s:
        return s
    chars = [""] * (len(s) * 2)
    for i, c in enumerate(s):
        chars[2 * i] = chr(ord(c) >> 8)
        chars[2 * i + 1] = chr(ord(c) & 0xff)
    return "".join(chars)

def main():
    with open("enc") as file:
        encrypted_flag = file.read()
        print(decrypt(encrypted_flag))

if __name__ == "__main__":
    main()
