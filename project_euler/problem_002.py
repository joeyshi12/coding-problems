def sum_even_fibonacci(n: int) -> int:
    if n <= 1:
        return 1

    prev = 1
    curr = 1
    acc = 0
    while curr <= n:
        if curr % 2 == 0:
            acc += curr
        prev, curr = curr, curr + prev
    return acc


def main():
    result = sum_even_fibonacci(4_000_000)
    print(result)


if __name__ == '__main__':
    main()
