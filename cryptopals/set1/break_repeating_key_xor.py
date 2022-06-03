import base64
from typing import List, Tuple
from single_byte_xor_cipher import decrypt_single_char_xor


def hamming_distance(s1: bytes, s2: bytes) -> int:
    assert len(s1) == len(s2)
    dist = 0
    for b1, b2 in zip(s1, s2):
        num = b1 ^ b2
        while num > 0:
            dist += num % 2
            num >>= 1
    return dist


def sort_key_sizes(ciphertext: bytes) -> List[Tuple[float, int]]:
    key_sizes = []
    for key_size in range(2, 41):
        dist = hamming_distance(ciphertext[:key_size], ciphertext[key_size:2 * key_size])
        key_sizes.append((dist / key_size, key_size))
    key_sizes.sort(reverse=True)
    return key_sizes


def main():
    # TODO: make this work
    ciphertext = b""
    with open("6.txt", encoding="utf-8") as f:
        ciphertext = base64.b64decode("".join(f.read().split()))

    key_sizes = sort_key_sizes(ciphertext)
    max_iters = 4
    for _ in range(max_iters):
        if not key_sizes:
            break
        _, key_size = key_sizes.pop()
        single_byte_xor_strings = [
            bytes([ciphertext[i * key_size + j] for i in range(len(ciphertext) // key_size)])
            for j in range(key_size)
        ]
        key = [decrypt_single_char_xor(text)[1] for text in single_byte_xor_strings]
        plaintext = bytes([c ^ key[(i + 2) % len(key)] for i, c in enumerate(ciphertext)])
        print(plaintext)


if __name__ == "__main__":
    main()
