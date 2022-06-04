# https://leetcode.com/problems/n-queens/

import unittest
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    return []


def is_valid_solution(board: List[str]) -> bool:
    return False


class TestSolveNQueens(unittest.TestCase):
    def test_single(self):
        result = solve_n_queens(1)
        expected = [["Q"]]
        self.assertEqual(result, expected)

    def test_multiple_solutions(self):
        result = solve_n_queens(4)
        expected = [[".Q..", "...Q", "Q...", "..Q."],
                    ["..Q.", "Q...", "...Q", ".Q.."]]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
