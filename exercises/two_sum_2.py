from typing import List
import unittest

def two_sum(nums: List[int], target: int) -> List[int]:
    i = 0
    j = len(nums) - 1
    while i < j:
        sum = nums[i] + nums[j]
        if sum == target:
            return [i + 1, j + 1]
        if sum < target:
            i += 1
        else:
            j -= 1
    return []

class TestTwoSum(unittest.TestCase):
    TEST_DATA = [
        (([2, 7, 11, 15], 9), [1, 2]),
        (([2, 3, 4], 6), [1, 3]),
        (([-1, 0], -1), [1, 2])
    ]

    def test_two_sum(self):
        for (nums, target), expected in self.TEST_DATA:
            result = two_sum(nums, target)
            self.assertListEqual(
                sorted(result),
                sorted(expected)
            )

if __name__ == "__main__":
    unittest.main()
