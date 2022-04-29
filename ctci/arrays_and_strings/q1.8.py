from typing import List, Set
import unittest

def zero_matrix(M: List[List[int]]) -> List[List[int]]:
    validate_matrix(M)
    if len(M) == 0 or len(M[0]) == 0:
        return M
    m, n = len(M), len(M[0])
    zero_rows = set()
    zero_cols = set()
    for i in range(m):
        for j in range(n):
            if M[i][j] == 0 and i not in zero_rows and j not in zero_cols:
                zero_matrix_row(M, i, zero_rows, zero_cols)
    return M

def zero_matrix_row(M: List[List[int]], i: int, zero_rows: Set[int], zero_cols: Set[int]) -> None:
    zero_rows.add(i)
    for j in range(len(M[0])):
        if M[i][j] == 0 and j not in zero_cols:
            zero_matrix_col(M, j, zero_rows, zero_cols)
        M[i][j] = 0

def zero_matrix_col(M: List[List[int]], j: int, zero_rows: Set[int], zero_cols: Set[int]) -> None:
    zero_cols.add(j)
    for i in range(len(M)):
        if M[i][j] == 0 and i not in zero_rows:
            zero_matrix_row(M, i, zero_rows, zero_cols)
        M[i][j] = 0

def validate_matrix(M):
    n = 0 if len(M) == 0 else len(M[0])
    for row in M:
        if len(row) != n:
            raise Exception("invalid matrix")

class TestZeroMatrix(unittest.TestCase):
    def test_empty(self):
        result = zero_matrix([])
        self.assertMatrixEqual(result, [])

    def test_one_by_one(self):
        result = zero_matrix([[1]])
        self.assertMatrixEqual(result, [[1]])

    def test_two_by_two(self):
        matrix = [[0, 1],
                  [2, 3]]
        result = zero_matrix(matrix)
        expected = [[0, 0],
                    [0, 3]]
        self.assertMatrixEqual(result, expected)

    def test_multiple_zeros_in_row(self):
        matrix = [[0, 1, 0, 3],
                  [4, 5, 6, 7],
                  [8, 9, 1, 2]]
        result = zero_matrix(matrix)
        expected = [[0, 0, 0, 0],
                    [0, 5, 0, 7],
                    [0, 9, 0, 2]]
        self.assertMatrixEqual(result, expected)

    def test_multiple_zeros_in_col(self):
        matrix = [[1, 1, 0, 3],
                  [2, 5, 6, 7],
                  [8, 9, 0, 2]]
        result = zero_matrix(matrix)
        expected = [[0, 0, 0, 0],
                    [2, 5, 0, 7],
                    [0, 0, 0, 0]]
        self.assertMatrixEqual(result, expected)

    def test_multiple_zeros(self):
        matrix = [[1, 1, 0, 3],
                  [2, 5, 6, 7],
                  [0, 9, 1, 2]]
        result = zero_matrix(matrix)
        expected = [[0, 0, 0, 0],
                    [0, 5, 0, 7],
                    [0, 0, 0, 0]]
        self.assertMatrixEqual(result, expected)

    def assertMatrixEqual(self, actual: List[List[int]], expected: List[List[int]]):
        self.assertEqual(len(actual), len(expected))
        if not actual:
            return
        cols = len(actual[0])
        for row1, row2 in zip(actual, expected):
            self.assertEqual(len(row1), cols)
            self.assertEqual(len(row2), cols)
            for a, b in zip(row1, row2):
                self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()
