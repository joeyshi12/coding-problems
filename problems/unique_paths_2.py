# https://leetcode.com/problems/unique-paths-ii/

"""
Let M be the obstacle grid and S[i][j] be the number of unique paths from (0, 0) to (i, j).
Then, S[i][j] can be expressed with the following recurrance relation:

          { 0,                          i < 0 or j < 0 or M[i][j] == 1
S[i][j] = { 1,                          i == j == 0 and M[0][0] == 0
          { S[i-1][j] + S[i][j - 1],    else
"""

import unittest
from typing import List


def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    if grid[0][0]:
        return 0
    m, n = len(grid), len(grid[0])
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    cache[1][1] = 1
    for i, row in enumerate(grid, start=1):
        for j, _ in enumerate(row, start=1):
            if i == j == 1 or grid[i - 1][j - 1]:
                continue
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
    return cache[m][n]


class TestUniquePathsWithObstacles(unittest.TestCase):
    TEST_DATA = [
        ([[0,1],[0,0]], 1),
        ([[0,0,0],[0,1,0],[0,0,0]], 2)
    ]

    def test_unique_paths_with_obstacles(self):
        for grid, expected in self.TEST_DATA:
            result = unique_paths_with_obstacles(grid)
            print(f"{grid} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
