# https://leetcode.com/problems/coin-change/

from typing import List
import unittest


def coin_change(coins: List[int], amount: int) -> int:
    inf = float("inf")
    cache = [inf] * (amount + 1)
    cache[0] = 0
    for i in range(1, amount + 1):
        cache[i] = min(1 + cache[i - coin] if i - coin >= 0 else inf for coin in coins)
    return cache[amount] if cache[amount] != inf else -1


class TestCoinChange(unittest.TestCase):
    TEST_DATA = [
        (([2], 3), -1),
        (([1], 3), 3),
        (([1, 2, 5], 11), 3),
    ]

    def test_coin_change(self):
        for (coins, amount), expected in self.TEST_DATA:
            result = coin_change(coins, amount)
            print(f"{coins, amount} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
