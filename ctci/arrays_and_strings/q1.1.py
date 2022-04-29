import unittest

def is_unique_1(s: str) -> bool:
    return len(s) == len(set(s))

def is_unique_2(s: str) -> bool:
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

class TestIsUnique(unittest.TestCase):
    TEST_DATA = [
        ("", True),
        ("a", True),
        ("aa", False),
        ("abc", True)
    ]

    def test_is_unique(self):
        for s, expected in self.TEST_DATA:
            self.assertEqual(is_unique_1(s), expected)
            self.assertEqual(is_unique_2(s), expected)

if __name__ == "__main__":
    unittest.main()
