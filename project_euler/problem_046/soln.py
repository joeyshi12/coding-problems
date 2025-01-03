# TODO
import math

is_prime_map = {}
is_square_map = {}


def is_prime(num: int) -> bool:
    if num in is_prime_map:
        return is_prime_map[num]
    for i in range(2, math.floor(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            is_prime_map[num] = False
            return False
    is_prime_map[num] = True
    return True


def is_square(num: int) -> bool:
    root = 1
    square = 1
    while square < num:
        square = root * root
        if square == num:
            is_square_map[num] = True
            return True
        root += 1
    is_square_map[num] = False
    return False


def satisfies(n: int) -> bool:
    for b in range(2, n, 2):
        a = n - b
        if is_prime(a) and is_square(b // 2):
            print(a, b)
            return False
    return True


for n in range(9, 1000, 2):
    if is_prime(n):
        continue
    if satisfies(n):
        print(n)
        break
        
