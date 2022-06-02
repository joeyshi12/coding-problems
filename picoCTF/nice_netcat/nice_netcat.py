# https://play.picoctf.org/practice/challenge/156

import subprocess

FLAG_FILE = "enc"
ARGV = ["nc", "mercury.picoctf.net", "22342"]

def main():
    subprocess.call(ARGV, stdout=open(FLAG_FILE, "w"))
    with open(FLAG_FILE) as file:
        flag = [chr(int(s)) for s in file.read().split()]
        print("".join(flag))

if __name__ == "__main__":
    main()
