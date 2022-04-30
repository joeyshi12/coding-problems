# https://leetcode.com/problems/rotate-image/

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    transpose(matrix)
    for row in matrix:
        reverse(row)

def transpose(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]

def reverse(nums: List[int]) -> None:
    for i in range(len(nums) // 2):
        nums[i], nums[-1 - i] = nums[-1 - i], nums[i]

# TODO: add tests
