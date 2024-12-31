divisor_sum_map = {}

def divisor_sum(num: int) -> int:
    if num in divisor_sum_map:
        return divisor_sum_map[num]
    result = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result += i
    divisor_sum_map[num] = result
    return divisor_sum_map[num]


def is_amicable(num: int) -> bool:
    return divisor_sum(divisor_sum(num)) == num


result = 0
for i in range(1, 10000):
    j = divisor_sum(i)
    if i != j and divisor_sum(j) == i:
        result += i
print(result)
