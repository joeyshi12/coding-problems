# https://leetcode.com/problems/merge-intervals/

from typing import List
import unittest

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) < 2:
        return intervals
    intervals.sort()
    merged_intervals = []
    current_interval = intervals[0]
    for i in range(1, len(intervals)):
        _, b1 = current_interval
        a2, b2 = intervals[i]
        if b1 >= a2:
            current_interval[1] = max(b1, b2)
        else:
            merged_intervals.append(current_interval)
            current_interval = intervals[i]
        if i == len(intervals) - 1:
            merged_intervals.append(current_interval)
    return merged_intervals

class TestMerge(unittest.TestCase):
    # TODO: add more tests
    TEST_DATA = [
        ([[1,4],[4,5]], [[1, 5]]),
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]])
    ]

    def test_merge(self):
        for intervals, expected in self.TEST_DATA:
            result = merge(intervals)
            result.sort()
            expected.sort()
            self.assertListEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
