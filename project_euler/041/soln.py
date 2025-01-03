import math
import itertools

is_prime_map = {}


def is_prime(num: int) -> bool:
    if num in is_prime_map:
        return is_prime_map[num]
    for i in range(2, math.floor(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            return False
    return True


max_pandigital_prime = 0
for n in range(9, 1, -1):
    for digits in itertools.permutations(range(n, 0, -1)):
        if digits[0] == 0:
            continue

        # Convert digits to number
        num = 0
        multiplier = 1
        for i in range(n - 1, -1, -1):
            num += digits[i] * multiplier
            multiplier *= 10

        if is_prime(num) and num > max_pandigital_prime:
            max_pandigital_prime = num

    if max_pandigital_prime != 0:
        break

print(max_pandigital_prime)
