"""
Given an array of at least 3 points from the xy plane stored in counter-clockwise order,
find the point with the largest y-coordinate within O(log(n)) runtime.
"""

import unittest
from typing import List
from enum import Enum, auto
import numpy as np


class Trend(Enum):
    TOP = auto()
    BOTTOM = auto()
    UPWARD = auto()
    DOWNWARD = auto()

def find_top(points: List[List[float]], low: int, high: int) -> int:
    if trend(points, low) == Trend.TOP:
        return low
    if trend(points, high) == Trend.TOP:
        return high
    p = (low + high) // 2
    if trend(points, p) == Trend.TOP:
        return p
    if trend(points, p) == Trend.UPWARD and trend(points, high) == Trend.DOWNWARD:
        return find_top(points, p + 1, high)
    return find_top(points, low, p - 1)

def trend(points: List[List[float]], i: int) -> Trend:
    forward = points[(i + 1) % len(points)]
    back = points[(i - 1) % len(points)]
    if points[i][1] < back[1]:
        if points[i][1] < forward[1]:
            return Trend.BOTTOM
        return Trend.DOWNWARD
    if points[i][1] > forward[1]:
        return Trend.TOP
    return Trend.UPWARD

class TestFindTop(unittest.TestCase):
    def test_find_top(self):
        angles = np.random.uniform(0, 2 * np.pi, size=16)
        angles.sort()
        x = np.cos(angles)
        y = np.sin(angles)
        point_list = np.column_stack((x, y))
        top = find_top(point_list, 0, len(point_list) - 1)
        self.assertEqual(y[top], max(y))

if __name__ == '__main__':
    unittest.main()
