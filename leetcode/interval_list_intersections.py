# https://leetcode.com/problems/interval-list-intersections/

from typing import List
import unittest

def interval_intersection(first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
    if not first_list or not second_list:
        return []
    intersections = []
    i = 0
    j = 0
    while i < len(first_list) and j < len(second_list):
        a1, b1 = first_list[i]
        a2, b2 = second_list[j]
        lower = max(a1, a2)
        upper = min(b1, b2)
        if lower <= upper:
            intersections.append([lower, upper])
        if j > len(second_list) - 1 or b2 >= b1:
            i += 1
        else:
            j += 1
    return intersections

class TestIntervalIntersection(unittest.TestCase):
    def test_empty(self):
        result = interval_intersection([], [])
        self.assertListEqual(result, [])

    def test_empty_first_list(self):
        first_list = []
        second_list = [[1, 3], [5, 9]]
        result = interval_intersection(first_list, second_list)
        self.assertListEqual(result, [])

    def test_empty_second_list(self):
        first_list = [[1, 3], [5, 9]]
        second_list = []
        result = interval_intersection(first_list, second_list)
        self.assertListEqual(result, [])

    def test_non_empty(self):
        first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
        second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
        result = interval_intersection(first_list, second_list)
        expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        self.assertListEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
