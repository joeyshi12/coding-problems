from typing import Dict


def chain_length(n: int, chain_lengths: Dict[int, int]) -> int:
    if n == 1:
        return 1
    if n not in chain_lengths:
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        chain_lengths[n] = 1 + chain_length(next_n, chain_lengths)
    return chain_lengths[n]


def main():
    argmax = -1
    longest_chain_length = 0
    chain_lengths = {}
    for num in range(1, 1_000_000):
        length = chain_length(num, chain_lengths)
        print(num, length)
        if length > longest_chain_length:
            argmax = num
            longest_chain_length = length

    print(f"Longest length = {longest_chain_length}")
    print(f"Starting number = {argmax}")


if __name__ == '__main__':
    main()
