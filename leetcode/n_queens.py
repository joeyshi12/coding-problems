# https://leetcode.com/problems/n-queens/

import unittest
from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    # TODO: you're too slow!
    solutions = []
    queen_positions = []
    __solve_n_queens(n, queen_positions, solutions, 0, -1)
    return [to_n_queens_board(n, positions) for positions in solutions]


def __solve_n_queens(n: int, queen_positions: List[List[int]], solutions: List[List[str]], p: int, q: int):
    if len(queen_positions) == n:
        print_board(to_n_queens_board(n, queen_positions))
        solutions.append(queen_positions.copy())
        return
    for i in range(p, n):
        for j in range(n):
            if i == p and j <= q:
                continue
            if is_valid_next_index(queen_positions, i, j):
                queen_positions.append([i, j])
                __solve_n_queens(n, queen_positions, solutions, i, j)
                queen_positions.pop()


def is_valid_next_index(queen_positions: List[List[int]], i: int, j: int) -> bool:
    return all(p != i and q != j and abs(p - i) != abs(q - j) for p, q in queen_positions)


def to_n_queens_board(n: int, positions: List[List[int]]) -> List[str]:
    board = [["."] * n for _ in range(n)]
    for i, j in positions:
        board[i][j] = "Q"
    return ["".join(row) for row in board]


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
    solve_n_queens(9)
    #unittest.main()
