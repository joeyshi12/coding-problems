def prime_factorize(n: int):
    prime_factors = []
    exponent = 0
    curr = 2
    while True:
        if n % curr == 0:
            n //= curr
            exponent += 1
        else:
            if exponent > 0:
                prime_factors.append((curr, exponent))
            if n == 1:
                break
            curr += 1
            exponent = 0
    return prime_factors


def main():
    n = 20
    largest_prime_exponents = {}
    for num in range(2, n + 1):
        factors = prime_factorize(num)
        for prime, exponent in factors:
            if prime not in largest_prime_exponents or largest_prime_exponents[prime] < exponent:
                largest_prime_exponents[prime] = exponent

    answer = 1
    for prime, exponent in largest_prime_exponents.items():
        answer *= prime ** exponent
    print(answer)


if __name__ == '__main__':
    main()
