# https://cryptopals.com/sets/1/challenges/2

import base64


def fixed_xor(s1: bytes, s2: bytes) -> bytes:
    hex_string1 = base64.b16decode(s1, casefold=True)
    hex_string2 = base64.b16decode(s2, casefold=True)
    message_bytes = bytes([b1 ^ b2 for b1, b2 in zip(hex_string1, hex_string2)])
    print(message_bytes)
    return base64.b16encode(message_bytes).lower()


def main():
    s1 = b"1c0111001f010100061a024b53535009181c"
    s2 = b"686974207468652062756c6c277320657965"
    expected = b"746865206b696420646f6e277420706c6179"

    assert fixed_xor(s1, s2) == expected
    print("Test pass!")


if __name__ == "__main__":
    main()
