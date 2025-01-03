import itertools

def compute_score(message: str) -> float:
    score = 0
    for char in message:
        if char in "aeiou":
            score += 1
            continue
        if char in " ":
            score += 0.1
            continue
        if char in ",.'/-":
            score += 0.05
            continue
        if char.isalpha():
            score += 0.5
            continue
        if char.isdigit():
            score += 0.2
            continue
        score -= 2
    return score


def decrypt(encrypted_bytes: list[int], key_bytes: list[int]) -> list[int]:
    return [byte ^ key_bytes[i % len(key_bytes)] for i, byte in enumerate(encrypted_bytes)]


with open("0059_cipher.txt", "r") as file:
    encrypted_bytes = [int(num) for num in file.read().strip("\n").split(",")]

    # ATTEMPT 1
    #score_and_messages = []
    #for key_chars in itertools.combinations("abcdefghijklmnopqrstuvwxyz", 3):
    #    key = [ord(char) for char in key_chars]
    #    decrypted_bytes = decrypt(encrypted_bytes, key)
    #    message = "".join([chr(byte) for byte in decrypted_bytes])
    #    message_score = compute_score(message)
    #    score_and_messages.append((message_score, "".join(key_chars), message))

    #score_and_messages.sort(key=lambda pair: pair[0])
    #for score, key, message in score_and_messages:
    #    print(message)

    # ATTEMPT 2
    #for char in "abcdefghijklmnopqrstuvwxyz":
    #    key_bytes = [ord("e"), ord(char), ord("p")]
    #    decrypted_bytes = decrypt(encrypted_bytes, key_bytes)
    #    print("".join([chr(byte) for byte in decrypted_bytes]))

    # After discovering the key:
    key_bytes = [ord("e"), ord("x"), ord("p")]
    decrypted_bytes = decrypt(encrypted_bytes, key_bytes)
    #message = "".join([chr(byte) for byte in decrypted_bytes])
    print(sum(decrypted_bytes))
