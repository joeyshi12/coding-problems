# https://leetcode.com/problems/container-with-most-water/

from typing import List
import unittest

def max_area(height: List[int]) -> int:
    # TODO: implement an O(n) solution
    max_capacity = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(height[i], height[j])
            if area > max_capacity:
                max_capacity = area
    return max_capacity

class TestMaxArea(unittest.TestCase):
    TEST_DATA = [
        ([], 0),
        ([1], 0),
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
