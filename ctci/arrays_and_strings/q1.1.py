import unittest

def is_unique_A(s):
    return len(s) == len(set(s))

def is_unique_B(s):
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
            self.assertEqual(is_unique_A(s), expected)
            self.assertEqual(is_unique_B(s), expected)

if __name__ == "__main__":
    unittest.main()
