import tqdm
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


def func(n: int, a: int, b: int) -> int:
    return n * n + a * n + b


argmax = None
max_consecutive_primes = 0
for a in tqdm.tqdm(range(-999, 1000)):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(func(n, a, b)):
            n += 1
        consecutive_primes = n + 1
        if max_consecutive_primes < consecutive_primes:
            argmax = (a, b)
            max_consecutive_primes = consecutive_primes

if argmax:
    print(f"Max consecutive primes = {max_consecutive_primes}")
    a, b = argmax
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a * b = {a * b}")
