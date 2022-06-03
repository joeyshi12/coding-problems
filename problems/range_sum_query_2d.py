# https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List
import unittest


class NumMatrix:
    regionSums: List[List[int]]

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.regionSums = [[0] * n for _ in range(m)]
        self.regionSums[0][0] = matrix[0][0]
        for i in range(1, m):
            self.regionSums[i][0] = self.regionSums[i - 1][0] + matrix[i][0]
        for j in range(1, n):
            self.regionSums[0][j] = self.regionSums[0][j - 1] + matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                self.regionSums[i][j] = matrix[i][j] + self.regionSums[i - 1][j] + self.regionSums[i][j - 1] - self.regionSums[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.regionSums[row2][col2]
        if row1 > 0:
            result -= self.regionSums[row1 - 1][col2]
        if col1 > 0:
            result -= self.regionSums[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            result += self.regionSums[row1 - 1][col1 - 1]
        return result


class TestNumMatrix(unittest.TestCase):
    def test_singleton(self):
        numMatrix = NumMatrix([[1]])
        result = numMatrix.sumRegion(0, 0, 0, 0)
        expected = 1
        self.assertEqual(result, expected)

    def test_row(self):
        numMatrix = NumMatrix([[1, 2, 3, 4]])
        self.assertEqual(numMatrix.sumRegion(0, 0, 0, 0), 1)
        self.assertEqual(numMatrix.sumRegion(0, 0, 0, 3), 10)
        self.assertEqual(numMatrix.sumRegion(0, 1, 0, 2), 5)

    def test_col(self):
        numMatrix = NumMatrix([[1], [2], [3], [4]])
        self.assertEqual(numMatrix.sumRegion(0, 0, 0, 0), 1)
        self.assertEqual(numMatrix.sumRegion(0, 0, 3, 0), 10)
        self.assertEqual(numMatrix.sumRegion(1, 0, 2, 0), 5)

    def test_matrix(self):
        numMatrix = NumMatrix([[1, 2, 3, 4],
                               [5, 6, 7, 8],
                               [9, 10, 11, 12],
                               [13, 14, 15, 16]])
        result = numMatrix.sumRegion(0, 0, 3, 3)
        expected = 16 * 17 // 2
        self.assertEqual(result, expected)

        result = numMatrix.sumRegion(1, 2, 3, 3)
        expected = 69
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
