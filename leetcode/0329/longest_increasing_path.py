# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

import unittest
from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    longest_path_length = 0
    cache = [[0] * len(row) for row in matrix]
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            path_length = __longest_increasing_path(matrix, i, j, cache)
            if path_length > longest_path_length:
                longest_path_length = path_length
    return longest_path_length


def __longest_increasing_path(matrix: List[List[int]], row: int, col: int, cache: List[List[int]]) -> int:
    if not cache[row][col]:
        longest_length = 1
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if row + i < 0 or row + i >= len(matrix) or col + j < 0 or col + j >= len(matrix[0]):
                continue
            if matrix[row][col] < matrix[row + i][col + j]:
                length = 1 + __longest_increasing_path(matrix, row + i, col + j, cache)
                if length > longest_length:
                    longest_length = length
        cache[row][col] = longest_length
    return cache[row][col]


class TestLongestIncreasingPath(unittest.TestCase):
    TEST_DATA = [
        ([[1]], 1),
        ([[3,4,5],[3,2,6],[2,2,1]], 4),
        ([[9,9,4],[6,6,8],[2,1,1]], 4)
    ]

    def test_longest_increasing_path(self):
        for matrix, expected in self.TEST_DATA:
            result = longest_increasing_path(matrix)
            print(f"{matrix} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
