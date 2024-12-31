from typing import List


def prime_factorize(n: int) -> List[int]:
    primes = []
    curr = 2
    while n > 1:
        if n % curr == 0:
            primes.append(curr)
            n //= curr
        else:
            curr += 1
    return primes


def main():
    n = 600851475143
    primes = prime_factorize(n)
    print(f"Prime factorization: {primes}")
    print(f"Largest prime: {max(primes)}")


if __name__ == '__main__':
    main()
