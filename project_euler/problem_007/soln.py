def nth_prime(n: int):
    primes = []
    num = 2
    while len(primes) < n:
        print(len(primes))
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 1
    return primes[-1]


def main():
    n = 10001
    print(nth_prime(n))


if __name__ == '__main__':
    main()
