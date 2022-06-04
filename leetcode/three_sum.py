# https://leetcode.com/problems/3sum/

from typing import List
import unittest

def three_sum(nums: List[int]) -> List[List[int]]:
    triples = []
    nums.sort()
    i = 0
    while i < len(nums):
        target = -nums[i]
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[j] + nums[k] == target:
                triples.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] + nums[k] == target:
                    j += 1
            while j < k and nums[j] + nums[k] < target:
                j += 1
            while j < k and nums[j] + nums[k] > target:
                k -= 1
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return triples

def sort_matrix(matrix):
    for row in matrix:
        row.sort()
    matrix.sort()

class TestThreeSum(unittest.TestCase):
    TEST_DATA = [
        ([], []),
        ([0, 0, 0], [[0, 0 ,0]]),
        ([0, -1, 1], [[0, -1, 1]]),
        ([0, -1, 1, 1], [[0, -1, 1]]),
        ([0, -1, 1, 1, -2], [[0, -1, 1], [1, 1, -2]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    ]

    def test_three_sum(self):
        for nums, expected in self.TEST_DATA:
            result = three_sum(nums)
            sort_matrix(result)
            sort_matrix(expected)
            self.assertEqual(len(result), len(expected))
            for row1, row2 in zip(result, expected):
                self.assertListEqual(row1, row2)
            print(f"{nums} -> {expected}")

if __name__ == "__main__":
    unittest.main()
