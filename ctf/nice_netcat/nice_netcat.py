# https://play.picoctf.org/practice/challenge/156

import subprocess

FLAG_FILE = "enc"
ARGV = ["nc", "mercury.picoctf.net", "22342"]

def to_flag_char(s: str) -> str:
    trimmed_str = s.strip()
    if not trimmed_str.isdigit():
        return ""
    return chr(int(trimmed_str))

def main():
    subprocess.call(ARGV, stdout=open(FLAG_FILE, "w"))
    with open(FLAG_FILE) as file:
        flag = map(to_flag_char, file.read().split("\n"))
        flag = filter(lambda s: s, flag)
        print("".join(flag))

if __name__ == "__main__":
    main()
