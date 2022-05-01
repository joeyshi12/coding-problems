# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List, Tuple
import unittest

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    tl = (0, 0)
    br = (len(matrix) - 1, len(matrix[0]) - 1)
    return search_slice(tl, br, matrix, target)

def search_slice(tl: Tuple[int, int],
                 br: Tuple[int, int],
                 matrix: List[List[int]],
                 target: int) -> bool:
    if not target_may_exist(target, tl, br, matrix):
        return False
    i = (tl[0] + br[0]) // 2
    j = (tl[1] + br[1]) // 2
    return search_row(i, tl[1], br[1], matrix, target) \
        or search_col(j, tl[0], br[0], matrix, target) \
        or search_slice(tl, (i - 1, j - 1), matrix, target) \
        or search_slice((tl[0], j + 1), (i - 1, br[1]), matrix, target) \
        or search_slice((i + 1, tl[1]), (br[0], j - 1), matrix, target) \
        or search_slice((i + 1, j + 1), br, matrix, target)

def target_may_exist(target: int,
                     tl: Tuple[int, int],
                     br: Tuple[int, int],
                     matrix: List[List[int]]) -> bool:
    i1, j1 = tl
    i2, j2 = br
    return 0 <= i1 <= i2 < len(matrix) \
        and 0 <= j1 <= j2 < len(matrix[0]) \
        and matrix[i1][j1] <= target <= matrix[i2][j2]

def search_row(row: int,
               start: int,
               end: int,
               matrix: List[List[int]],
               target: int) -> bool:
    while start <= end:
        p = (start + end) // 2
        if matrix[row][p] == target:
            return True
        if matrix[row][p] < target:
            start = p + 1
        else:
            end = p - 1
    return False

def search_col(col: int,
               start: int,
               end: int,
               matrix: List[List[int]],
               target: int) -> bool:
    while start <= end:
        p = (start + end) // 2
        if matrix[p][col] == target:
            return True
        if matrix[p][col] < target:
            start = p + 1
        else:
            end = p - 1
    return False

class TestSearchMatrix(unittest.TestCase):
    def test_empty(self):
        result = search_matrix([], 0)
        self.assertFalse(result)

    def test_row(self):
        matrix = [[-1,3]]
        result = search_matrix(matrix, 1)
        self.assertFalse(result)

    def test_square_exists(self):
        matrix = [[1, 4, 7, 11, 15],
                  [2, 5, 8, 12, 19],
                  [3, 6, 9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]]
        result = search_matrix(matrix, 5)
        self.assertTrue(result)

    def test_square_exists_2(self):
        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        result = search_matrix(matrix, 5)
        self.assertTrue(result)

    def test_square_not_exists(self):
        matrix = [[1, 4, 7, 11, 15],
                  [2, 5, 8, 12, 19],
                  [3, 6, 9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]]
        result = search_matrix(matrix, 20)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
