# https://leetcode.com/problems/container-with-most-water/

from typing import List
import unittest

def max_area(height: List[int]) -> int:
    max_capacity = 0
    i = 0
    j = len(height) - 1
    while i < j:
        capacity = min(height[i], height[j]) * (j - i)
        if capacity > max_capacity:
            max_capacity = capacity
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_capacity

class TestMaxArea(unittest.TestCase):
    TEST_DATA = [
        ([1, 1], 1),
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    ]

    def test_max_area(self):
        for height, expected in self.TEST_DATA:
            result = max_area(height)
            print(f"{height} -> {expected}")
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
