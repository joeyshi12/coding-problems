# Implement repeating-key XOR
# https://cryptopals.com/sets/1/challenges/5

import base64


def repeating_key_xor_encrypt(text: str, key: str) -> bytes:
    text_bytes = bytearray(text, "ascii")
    key_bytes = bytes(key, "ascii")
    for i, byte in enumerate(text_bytes):
        text_bytes[i] = byte ^ key_bytes[i % len(key_bytes)]
    return base64.b16encode(text_bytes).lower()


def main():
    text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    expected = (b"0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
                b"a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

    assert repeating_key_xor_encrypt(text, key) == expected
    print("Test pass!")


if __name__ == "__main__":
    main()
