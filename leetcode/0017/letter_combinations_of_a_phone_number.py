# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import unittest
from typing import List
from collections import deque

LETTER_REP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    queue = deque(list(LETTER_REP[digits[0]]))
    while len(queue[0]) < len(digits):
        p = queue.popleft()
        for c in LETTER_REP[digits[len(p)]]:
            queue.append(p + c)
    return list(queue)


class TestLetterCombinations(unittest.TestCase):
    TEST_DATA = [
        ("", []),
        ("2", ["a", "b", "c"]),
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"])
    ]

    def test_letter_combinations(self):
        for digits, expected in self.TEST_DATA:
            result = letter_combinations(digits)
            result.sort()
            expected.sort()
            print(f"{digits} -> {result}")
            self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
