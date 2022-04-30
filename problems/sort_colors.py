# https://leetcode.com/problems/sort-colors/

from typing import List
import unittest

def sort_colors(nums: List[int]) -> None:
    if len(nums) < 2:
        return
    i = 0
    start = 0
    end = len(nums) - 1
    while i <= end:
        while (i > start and nums[i] == 0) or (i < end and nums[i] == 2):
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
            else:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
        i += 1

class TestSortColors(unittest.TestCase):
    TEST_DATA = [
        ([], []),
        ([1], [1]),
        ([2, 0, 1], [0, 1, 2]),
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    ]

    def test_sort_colors(self):
        for nums, expected in self.TEST_DATA:
            sort_colors(nums)
            print(nums)
            self.assertListEqual(nums, expected)

if __name__ == "__main__":
    unittest.main()
