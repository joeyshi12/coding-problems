# https://leetcode.com/problems/backspace-string-compare/

import unittest


def backspace_compare(s: str, t: str) -> bool:
    return __backspace_compare(s, t, len(s) - 1, len(t) - 1, 0, 0)


def __backspace_compare(s: str, t: str, i: int, j: int, skips_s: int, skips_t: int) -> bool:
    if i < 0 and j < 0:
        return True
    if i >= 0:
        if s[i] == "#":
            return __backspace_compare(s, t, i - 1, j, skips_s + 1, skips_t)
        if skips_s > 0:
            return __backspace_compare(s, t, i - 1, j, skips_s - 1, skips_t)
    if j >= 0:
        if t[j] == "#":
            return __backspace_compare(s, t, i, j - 1, skips_s, skips_t + 1)
        if skips_t > 0:
            return __backspace_compare(s, t, i, j - 1, skips_s, skips_t - 1)
    if (i < 0 and j >= 0) or (i >= 0 and j < 0) or s[i] != t[j]:
        return False
    return __backspace_compare(s, t, i - 1, j - 1, skips_s, skips_t)


class TestBackspaceCompare(unittest.TestCase):
    TEST_DATA = [
        (("ab#c", "ad#c"), True),
        (("ab##", "c#d#"), True),
        (("a#c", "b"), False),
        (("xywrrmp", "xywrrmu#p"), True)
    ]

    def test_backspace_compare(self):
        for (s, t), expected in self.TEST_DATA:
            result = backspace_compare(s, t)
            print(f"{s}, {t} -> {result}")
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
