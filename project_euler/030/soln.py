def is_valid(num: int) -> bool:
    power_sum = 0
    n = num
    while n > 0:
        digit = n % 10
        power_sum += digit ** 5
        n //= 10
    return num == power_sum


result = 0
for i in range(2, 1000000):
    if is_valid(i):
        result += i
print(result)
