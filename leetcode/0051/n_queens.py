# https://leetcode.com/problems/n-queens/

import unittest
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    solutions = []
    queens = [-1] * n

    def generate_solutions(row: int) -> None:
        if row == n:
            solutions.append(to_n_queens_board(n, queens))
            return
        for i in range(n):
            if is_valid_next_queen(queens, row, i):
                queens[row] = i
                generate_solutions(row + 1)

    generate_solutions(0)
    return solutions


def is_valid_next_queen(queens: List[int], row: int, col: int) -> bool:
    for i in range(row):
        if queens[i] == col or row - i == abs(col - queens[i]):
            return False
    return True


def to_n_queens_board(n: int, queens: List[int]) -> List[str]:
    return ["." * num + "Q" + "." * (n - 1 - num) for num in queens]


def print_board(board: List[str]) -> None:
    print("\n".join([" ".join(list(row)) for row in board]) + "\n")


class TestSolveNQueens(unittest.TestCase):
    def test_single(self):
        result = solve_n_queens(1)
        expected = [["Q"]]
        self.assertListEqual(result, expected)

    def test_multiple_solutions(self):
        result = solve_n_queens(4)
        expected = [[".Q..", "...Q", "Q...", "..Q."],
                    ["..Q.", "Q...", "...Q", ".Q.."]]
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
