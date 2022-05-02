# https://play.picoctf.org/practice/challenge/253

CHAR_MAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def decrypt(message: str) -> str:
    nums = filter(lambda s: s.isdigit(), message.split(" "))
    decrypted = map(lambda s: CHAR_MAP[int(s) % len(CHAR_MAP)], nums)
    return "".join(decrypted)

def main():
    with open("message.txt") as file:
        print(decrypt(file.read()))

if __name__ == "__main__":
    main()
