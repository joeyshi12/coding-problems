# https://leetcode.com/problems/backspace-string-compare/

import unittest

def backspace_compare(s: str, t: str) -> bool:
    skips_s = 0
    skips_t = 0
    i = len(s) - 1
    j = len(t) - 1
    while i >= 0 or j >= 0:
        while i >= 0 and (skips_s > 0 or s[i] == "#"):
            if s[i] == "#":
                skips_s += 1
            elif skips_s > 0:
                skips_s -= 1
            i -= 1
        while j >= 0 and (skips_t > 0 or t[j] == "#"):
            if t[j] == "#":
                skips_t += 1
            elif skips_t > 0:
                skips_t -= 1
            j -= 1
        if (i >= 0 and j < 0) or (i < 0 and j >= 0):
            return False
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        i -= 1
        j -= 1
    return True

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
