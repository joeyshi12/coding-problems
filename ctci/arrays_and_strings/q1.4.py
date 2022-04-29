import unittest

def is_palindrome_permutation(s: str) -> bool:
    counts = {}
    for c in s.lower():
        if c != " ":
            counts[c] = counts.get(c, 0) + 1
    odd_freqs = sum(freq % 2 for freq in counts.values())
    return odd_freqs < 2

class TestIsPalindromePermutation(unittest.TestCase):
    TEST_DATA = [
        ("", True),
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("aab", True),
        ("Tact Coa", True)
    ]

    def test_is_palindrome_permutation(self):
        for s, expected in self.TEST_DATA:
            self.assertEqual(is_palindrome_permutation(s), expected)
            print(f"\"{s}\" -> {expected}")

if __name__ == "__main__":
    unittest.main()
