import math

is_prime_map = {1: False}


def is_prime(n: int) -> bool:
    if n in is_prime_map:
        return is_prime_map[n]
    for i in range(2, math.floor(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            is_prime_map[n] = False
            return False
    is_prime_map[n] = True
    return True


def is_truncatable_prime(n: int) -> bool:
    if not is_prime(n):
        return False
    n_str = str(n)
    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[:i])):
            return False
        if not is_prime(int(n_str[i:])):
            return False
    return True


result = 0
for i in range(10, 1000000):
    if is_truncatable_prime(i):
        result += i
print(result)
