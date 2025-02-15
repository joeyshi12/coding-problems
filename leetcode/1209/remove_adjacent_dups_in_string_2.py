# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

import unittest


def remove_duplicates(s: str, k: int) -> str:
    return ""


class TestRemoveDuplicates(unittest.TestCase):
    TEST_DATA = [
        (("abcd", 2), "abcd"),
        (("deeedbbcccbdaa", 3), "aa"),
        (("pbbcggttciiippooaais", 2), "ps")
    ]

    def test_remove_duplicates(self):
        for (s, k), expected in self.TEST_DATA:
            result = remove_duplicates(s, k)
            print(f"{s}, {k} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
