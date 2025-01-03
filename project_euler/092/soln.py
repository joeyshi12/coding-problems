will_arrive_89_map = {}


def will_arrive_89(num: int) -> bool:
    if num == 1:
        return False
    if num == 89:
        return True
    if num in will_arrive_89_map:
        return will_arrive_89_map[num]

    result = 0
    for char in str(num):
        result += int(char) ** 2

    return will_arrive_89(result)


count = 0
for i in range(1, 10000000):
    if will_arrive_89(i):
        count += 1
print(count)
