# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List
import unittest

def generate_matrix(n: int) -> List[List[int]]:
    matrix = [None] * n
    for i in range(n):
        matrix[i] = [0] * n
    populate_right(0, 0, matrix, 1)
    return matrix

def populate_right(i: int, j: int, matrix: List[List[int]], counter: int) -> None:
    if counter > len(matrix) ** 2:
        return
    matrix[i][j] = counter
    if j >= len(matrix) - 1 - i:
        populate_down(i + 1, j, matrix, counter + 1)
    else:
        populate_right(i, j + 1, matrix, counter + 1)

def populate_down(i: int, j: int, matrix: List[List[int]], counter: int) -> None:
    if counter > len(matrix) ** 2:
        return
    matrix[i][j] = counter
    if i >= j:
        populate_left(i, j - 1, matrix, counter + 1)
    else:
        populate_down(i + 1, j, matrix, counter + 1)

def populate_left(i: int, j: int, matrix: List[List[int]], counter: int) -> None:
    if counter > len(matrix) ** 2:
        return
    matrix[i][j] = counter
    if j <= len(matrix) - 1 - i:
        populate_up(i - 1, j, matrix, counter + 1)
    else:
        populate_left(i, j - 1, matrix, counter + 1)

def populate_up(i: int, j: int, matrix: List[List[int]], counter: int) -> None:
    if counter > len(matrix) ** 2:
        return
    matrix[i][j] = counter
    if i <= j + 1:
        populate_right(i, j + 1, matrix, counter + 1)
    else:
        populate_up(i - 1, j, matrix, counter + 1)

class TestGenerateMatrix(unittest.TestCase):
    def test_zero(self):
        result = generate_matrix(0)
        self.assertEqual(result, [])

    def test_one(self):
        result = generate_matrix(1)
        self.assertEqual(result, [[1]])

    def test_two(self):
        result = generate_matrix(2)
        expected = [[1, 2],
                    [4, 3]]
        self.assertEqual(result, expected)

    def test_three(self):
        result = generate_matrix(3)
        expected = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
