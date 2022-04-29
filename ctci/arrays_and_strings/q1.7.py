from typing import List
import unittest

def rotate_matrix(M: List[List[int]]) -> List[List[int]]:
    validate_square(M)
    transpose(M)
    n = len(M)
    for i in range(n // 2):
        M[i], M[n - 1 - i] = M[n - 1 - i], M[i]
    return M

def transpose(M: List[List[int]]) -> None:
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j], M[j][i] = M[j][i], M[i][j]

def validate_square(M: List[List[int]]) -> None:
    n = len(M)
    for row in M:
        if len(row) != n:
            raise Exception

class TestRotateMatrix(unittest.TestCase):
    def test_zero_by_zero(self):
        matrix = []
        result = rotate_matrix(matrix)
        self.assertMatrixEqual(result, [])

    def test_one_by_one(self):
        matrix = [[1]]
        result = rotate_matrix(matrix)
        self.assertMatrixEqual(result, [[1]])

    def test_two_by_two(self):
        matrix = [[0, 1],
                  [2, 3]]
        result = rotate_matrix(matrix)
        expected = [[1, 3],
                    [0, 2]]
        self.assertMatrixEqual(result, expected)

    def test_three_by_three(self):
        matrix = [[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]]
        result = rotate_matrix(matrix)
        expected = [[2, 5, 8],
                    [1, 4, 7],
                    [0, 3, 6]]
        self.assertMatrixEqual(result, expected)

    def assertMatrixEqual(self, actual: List[List[int]], expected: List[List[int]]):
        validate_square(actual)
        validate_square(expected)
        self.assertEqual(len(actual), len(expected))
        for row1, row2 in zip(actual, expected):
            for a, b in zip(row1, row2):
                self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main()
