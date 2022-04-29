from typing import List
import unittest

def find_peak_element(nums: List[int]):
    if not nums:
        raise Exception("nums must be nonempty")
    i = 0
    j = len(nums) - 1
    while i <= j:
        p = (i + j) // 2
        if is_peak(p, nums):
            return p
        if p < len(nums) - 1 and nums[p] < nums[p + 1]:
            i = p + 1
        else:
            j = p - 1
    raise Exception("peak not found")

def is_peak(i, nums):
    if not nums:
        return False
    if len(nums) == 1:
        return i == 0
    if i == 0:
        return nums[0] > nums[1]
    if i == len(nums) - 1:
        return nums[-1] > nums[-2]
    return nums[i - 1] < nums[i] and nums[i] > nums[i + 1]

class TestFindPeakElement(unittest.TestCase):
    TEST_DATA = [
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5)
    ]

    def test_empty(self):
        self.assertRaises(Exception, find_peak_element, [])

    def test_find_peak_element(self):
        for nums, expected in self.TEST_DATA:
            result = find_peak_element(nums)
            self.assertEqual(result, expected)
            print(f"{nums} -> {expected}")

if __name__ == "__main__":
    unittest.main()
