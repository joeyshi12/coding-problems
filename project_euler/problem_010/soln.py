def prime_sum(n: int):
    primes = [2]
    num = 3
    while True:
        print(f"it: {num} / {n}")
        if all(num % prime != 0 for prime in primes):
            if num >= n:
                break
            primes.append(num)
        num += 1

    return sum(primes)


def main():
    n = 2_000_000
    print(f"prime_sum({n}) = {prime_sum(n)}")


if __name__ == '__main__':
    main()
