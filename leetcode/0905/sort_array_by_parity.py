# https://leetcode.com/problems/sort-array-by-parity/submissions/

from typing import List
import unittest

def sort_array_by_parity(nums: List[int]) -> List[int]:
    return list(filter(lambda num: num % 2 == 0, nums)) \
        + list(filter(lambda num: num % 2 == 1, nums))

class TestSortArrayByParity(unittest.TestCase):
    TEST_DATA = [
        ([0], [0]),
        ([3, 1, 2, 4], [2, 4, 3, 1])
    ]

    def test_sort_array_by_parity(self):
        for nums, expected in self.TEST_DATA:
            result = sort_array_by_parity(nums)
            print(f"{nums} -> {result}")
            self.assertListEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
