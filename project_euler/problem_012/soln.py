def triangle_number(n: int) -> int:
    return n * (n + 1) // 2


def num_divisors(n: int) -> int:
    result = 1
    num = 2
    exponent = 0
    while True:
        if n % num == 0:
            n = n // num
            exponent += 1
        else:
            result *= 1 + exponent
            if n == 1:
                break
            exponent = 0
            num += 1
    return result


def main():
    n = 1
    while True:
        tri_num = triangle_number(n)
        divs = num_divisors(tri_num)
        print(tri_num, divs)
        if divs > 500:
            print(tri_num)
            break
        n += 1


if __name__ == '__main__':
    main()
