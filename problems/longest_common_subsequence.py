# https://leetcode.com/problems/longest-common-subsequence/

import unittest


def longest_common_subsequence(text1: str, text2: str) -> int:
    cache = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i, c1 in enumerate(text1):
        for j, c2 in enumerate(text2):
            if c1 == c2:
                cache[i + 1][j + 1] = cache[i][j] + 1
            else:
                cache[i + 1][j + 1] = max(cache[i][j + 1], cache[i + 1][j])
    return cache[-1][-1]


class TestLongestCommonSubsequence(unittest.TestCase):
    TEST_DATA = [
        (("abc", "def"), 0),
        (("abc", "abc"), 3),
        (("abcde", "ace"), 3)
    ]

    def test_longest_common_subsequence(self):
        for (text1, text2), expected in self.TEST_DATA:
            result = longest_common_subsequence(text1, text2)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
