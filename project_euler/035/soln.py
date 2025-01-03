import math

is_prime_map = {}


def is_prime(n: int) -> bool:
    if n in is_prime_map:
        return is_prime_map[n]
    for i in range(2, math.floor(math.sqrt(abs(n))) + 1):
        if n % i == 0:
            is_prime_map[n] = False
            return False
    is_prime_map[n] = True
    return True


def is_circular_prime(p: int) -> bool:
    p_str = str(p)
    p_len = len(p_str)
    for i in range(p_len):
        p_rot = int(p_str[i:i+p_len] + p_str[:i])
        if not is_prime(p_rot):
            return False
    return True


print(sum(is_circular_prime(i) for i in range(2, 1000001)))
