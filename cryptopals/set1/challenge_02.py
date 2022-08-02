# Fixed XOR
# https://cryptopals.com/sets/1/challenges/2

import base64


def xor(s1: bytes, s2: bytes) -> bytes:
    return bytes([b1 ^ b2 for b1, b2 in zip(s1, s2)])


def main():
    s1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    s2 = bytes.fromhex("686974207468652062756c6c277320657965")
    expected = b"746865206b696420646f6e277420706c6179"

    xor_string = xor(s1, s2)
    print(xor_string)
    plaintext = base64.b16encode(xor_string).lower()
    assert plaintext == expected
    print("Test pass!")


if __name__ == "__main__":
    main()
