# Break repeating-key XOR
# https://cryptopals.com/sets/1/challenges/6

import base64
from typing import List
import challenge_03


def hamming_distance(s1: bytes, s2: bytes) -> int:
    assert len(s1) == len(s2)
    dist = 0
    for b1, b2 in zip(s1, s2):
        num = b1 ^ b2
        while num > 0:
            dist += num % 2
            num >>= 1
    return dist


def sorted_key_sizes(ciphertext: bytes) -> List[int]:
    # TODO: improve so that correct key size appears closer to top
    key_sizes = []
    for key_size in range(2, 41):
        dist = hamming_distance(ciphertext[:key_size], ciphertext[key_size:2 * key_size])
        normalized_dist = dist / key_size
        key_sizes.append((normalized_dist, key_size))
    key_sizes.sort()
    return [key for _, key in key_sizes]


def decrypt_repeating_key_xor(ciphertext: bytes, key_size: int) -> bytes:
    num_blocks = len(ciphertext) // key_size
    key = []
    for j in range(key_size):
        cipher_bytes = bytes([ciphertext[i * key_size + j] for i in range(num_blocks)])
        single_char_xor_key = challenge_03.decrypt_single_char_xor(cipher_bytes)[1]
        key.append(single_char_xor_key)

    plaintext = [0] * len(ciphertext)
    for i, _ in enumerate(ciphertext):
        plaintext[i] = ciphertext[i] ^ key[i % key_size]

    return bytes(plaintext)


def main():
    with open("./6.txt", encoding="utf-8") as f:
        ciphertext = base64.b64decode("".join(f.read().split()))

    #for key_size in sorted_key_sizes(ciphertext):
    #    message = decrypt_repeating_key_xor(ciphertext, key_size)
    #    print(key_size)
    #    print(message[:32])

    message = decrypt_repeating_key_xor(ciphertext, 29)
    print(message)


if __name__ == "__main__":
    main()
