coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count_coin_sums(remaining: int, i: int) -> int:
    if i < 0 or remaining < 0:
        return 0
    if remaining == 0:
        return 1
    return count_coin_sums(remaining - coins[i], i) + count_coin_sums(remaining, i - 1)


print(count_coin_sums(200, len(coins) - 1))
