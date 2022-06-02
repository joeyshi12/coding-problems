# https://play.picoctf.org/practice/challenge/254

CHAR_MAP = "\0ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

def mod_inverse(c: int, n: int) -> int:
    for i in range(1, n):
        if (i * c) % n == 1:
            return i
    return -1

def to_flag_char(num: int) -> str:
    return CHAR_MAP[mod_inverse(num % 41, 41)]

def main():
    with open("message.txt") as file:
        flag = [to_flag_char(int(s)) for s in file.read().split()]
        print("".join(flag))

if __name__ == "__main__":
    main()
