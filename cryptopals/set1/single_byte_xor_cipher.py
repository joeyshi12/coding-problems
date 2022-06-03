# https://cryptopals.com/sets/1/challenges/3

from typing import Tuple
import string


def get_score(message: bytes):
    score = 0
    for byte in message:
        c = chr(byte)
        if c in string.ascii_letters:
            score += 1
        elif c in string.whitespace:
            score += 0.75
        elif c in string.punctuation or c in string.digits:
            score += 0.5
        else:
            score -= 0.5
    return score


def decrypt_single_char_xor(ciphertext: bytes) -> Tuple[bytes, int, int]:
    message_bytes = b""
    key = -1
    best_score = -1
    for i in range(256):
        byte_str = bytes([byte ^ i for byte in ciphertext])
        score = get_score(byte_str)
        if score > best_score:
            message_bytes = byte_str
            key = i
            best_score = score
    return message_bytes, key, best_score


def main():
    hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = bytes.fromhex(hex_string)

    byte_string, _, _ = decrypt_single_char_xor(ciphertext)
    print(byte_string.decode("ascii"))


if __name__ == "__main__":
    main()
