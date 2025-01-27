# https://leetcode.com/problems/median-of-two-sorted-arrays/

import unittest
from typing import List


def find_median(nums1: List[int], nums2: List[int]) -> float:
    """Returns the median of sorted arrays nums1, nums2"""
    # TODO: implement
    return 0


class TestFindMedian(unittest.TestCase):
    TEST_DATA = [
        (([1], [2]), 1.5),
        (([1, 3], [2]), 2),
        (([1, 2], [3, 4]), 2.5)
    ]

    def test_find_median(self):
        for (nums1, nums2), expected in self.TEST_DATA:
            result = find_median(nums1, nums2)
            print(f"{nums1, nums2} -> {result}")
            self.assertAlmostEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
