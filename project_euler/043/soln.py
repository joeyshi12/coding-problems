import itertools

divisors = [2, 3, 5, 7, 11, 13, 17]


def has_divisibility_property(digits: tuple[int, ...]) -> bool:
    for i in range(7):
        num = digits[i + 1] * 100 + digits[i + 2] * 10 + digits[i + 3]
        if num % divisors[i] != 0:
            return False
    return True


result = 0
for digits in itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    if has_divisibility_property(digits):
        num = 0
        multiplier = 1
        for i in range(9, -1, -1):
            num += digits[i] * multiplier
            multiplier *= 10
        print(f"{num} satisfies the property")
        result += num
print(f"Sum of pandigital numbers with property = {result}")
