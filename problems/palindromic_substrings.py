# https://leetcode.com/problems/palindromic-substrings/

import unittest


def palindromic_substrings(s: str) -> int:
    # TODO: this is terrible, do better
    count = len(s)
    for i in range(len(s) - 1):
        r = 0
        while s[i - r] == s[i + 1 + r]:
            count += 1
            r += 1
            if i - r < 0 or i + 1 + r >= len(s):
                break
        if i == 0:
            continue
        r = 0
        while s[i - 1 - r] == s[i + 1 + r]:
            count += 1
            r += 1
            if i - 1 - r < 0 or i + 1 + r >= len(s):
                break
    return count


class TestPalindromicSubstrings(unittest.TestCase):
    TEST_DATA = [
        ("a", 1),
        ("aa", 3),
        ("aba", 4),
        ("abc", 3),
        ("xabax", 7)
    ]

    def test_palindromic_substrings(self):
        for s, expected in self.TEST_DATA:
            result = palindromic_substrings(s)
            print(f"{s} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
