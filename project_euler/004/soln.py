def main():
    n = 997799
    while n >= 100001:
        for i in range(999, 99, -1):
            if n % i == 0:
                j = n // i
                if 100 <= j < 1000:
                    print(f"Factors: {i, j}")
                    print(f"ANS: {i * j}")
                    return

        if (n // 100) % 10 > 0:
            n -= 1100
        elif (n // 10) % 10 > 0:
            n -= 10010
            n += 9900
        else:
            n -= 100001
            n += 99990


if __name__ == '__main__':
    main()
