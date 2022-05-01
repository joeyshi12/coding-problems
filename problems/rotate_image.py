# https://leetcode.com/problems/rotate-image/

from typing import List
import unittest

def rotate(matrix: List[List[int]]) -> None:
    validate_square(matrix)
    transpose(matrix)
    for row in matrix:
        reverse(row)

def transpose(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse(nums: List[int]) -> None:
    for i in range(len(nums) // 2):
        nums[i], nums[-1 - i] = nums[-1 - i], nums[i]

def validate_square(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise Exception("matrix is not square")

class TestRotate(unittest.TestCase):
    # TODO: add tests
    pass

if __name__ == "__main__":
    unittest.main()
