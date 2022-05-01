# https://leetcode.com/problems/pascals-triangle-ii/submissions/

from typing import List
import unittest

def get_row(row_index: int) -> List[int]:
    row = [0] * (row_index + 1)
    numerator = 1
    denominator = 1
    for i in range((row_index + 1) // 2 + 1):
        row[i] = row[-1-i] = numerator // denominator
        numerator *= row_index - i
        denominator *= i
    return row

class TestGetRow(unittest.TestCase):
    # TODO: add tests
    pass

if __name__ == "__main__":
    unittest.main()
