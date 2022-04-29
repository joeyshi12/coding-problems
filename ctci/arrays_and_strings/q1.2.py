import unittest

def check_permutation(a, b):
    if len(a) != len(b):
        return False
    counts = {}
    for valA, valB in zip(a, b):
        counts[valA] = counts.get(valA, 0) + 1
        counts[valB] = counts.get(valB, 0) - 1
    return all(count == 0 for count in counts.values())

class TestCheckPermutation(unittest.TestCase):
    TEST_DATA = [
        (("", ""), True),
        (("a", ""), False),
        (("a", "b"), False),
        (("a", "a"), True),
        (("ab", "ba"), True),
        (("acb", "bac"), True)
    ]

    def test_check_permutation(self):
        for (a, b), expected in self.TEST_DATA:
            self.assertEqual(check_permutation(a, b), expected)

if __name__ == "__main__":
    unittest.main()
