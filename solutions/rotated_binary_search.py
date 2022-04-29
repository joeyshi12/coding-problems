from typing import List, Callable
import unittest

def search(nums: List[int], target: int) -> int:
    m = find_arg_min(nums)
    if m == -1:
        return -1
    return rotated_binary_search(nums, target, m)

def rotated_binary_search(nums: List[int], target: int, shift: int) -> int:
    if not nums:
        return -1
    n = len(nums)
    i = 0
    j = n - 1
    while i <= j:
        p = (i + j) // 2
        ps = (p + shift) % n
        if nums[ps] == target:
            return ps
        if nums[ps] < target:
            i = p + 1
        else:
            j = p - 1
    return -1

def find_arg_min(nums: List[int]):
    if not nums:
        return -1
    i = 0
    j = len(nums) - 1
    while i <= j:
        p = (i + j) // 2
        if is_min_idx(p, nums):
            return p
        if nums[p] > nums[j]:
            i = p + 1
        else:
            j = p - 1
    return -1

def is_min_idx(i: int, nums: List[int]):
    return (i == 0 and nums[0] <= nums[-1]) \
        or (i > 0 and nums[i] < nums[i - 1])

class TestSearch(unittest.TestCase):
    TEST_DATA = [
        (([], 0), -1),
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        (([1], 0), -1)
    ]

    def test_search(self):
        for (nums, target), expected in self.TEST_DATA:
            self.assertEqual(search(nums, target), expected)
            print(f"{nums}, {target} -> {expected}")

if __name__ == "__main__":
    unittest.main()
