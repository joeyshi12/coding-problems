import tqdm

is_abundant_map: dict[int, bool] = {}


def is_abundant(num: int) -> bool:
    if num in is_abundant_map:
        return is_abundant_map[num]
    divisor_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisor_sum += i
    is_abundant_map[num] = divisor_sum > num
    return is_abundant_map[num]


def is_abundant_sum(num: int) -> bool:
    for a in range(12, num):
        b = num - a
        if is_abundant(a) and is_abundant(b):
            return True
    return False


result = 0
for i in tqdm.tqdm(range(1, 28123)):
    if not is_abundant_sum(i):
        result += i
print(result)
