import math

digit_factorials = [math.factorial(n) for n in range(10)]


def is_digit_factorial_sum(num: int) -> bool:
    digit_factorial_sum = 0
    n = num
    while n > 0:
        digit = n % 10
        digit_factorial_sum += digit_factorials[digit]
        n //= 10
    return num == digit_factorial_sum


result = 0
for i in range(10, 1000000):
    if is_digit_factorial_sum(i):
        result += i

print(result)
