# https://leetcode.com/problems/sudoku-solver/

from typing import List, Optional


def solveSudoku(board: List[List[str]]) -> None:
    # TODO: Make faster

    row_visited = [set() for _ in range(9)]
    col_visited = [set() for _ in range(9)]
    block_visited = [set() for _ in range(9)]
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                empty_cells.append((i, j))
    empty_cells.reverse()

    for row in range(9):
        for j in range(9):
            row_visited[row].add(board[row][j])

    for col in range(9):
        for i in range(9):
            col_visited[col].add(board[i][col])

    for block in range(9):
        i1 = (block // 3) * 3
        j1 = (block % 3) * 3
        for i2 in range(i1, i1 + 3):
            for j2 in range(j1, j1 + 3):
                block_visited[block].add(board[i2][j2])

    def solve() -> bool:
        empty_cell = findEmptyCell(board)
        if empty_cell is None:
            return True
        row, col = empty_cell
        block = (row // 3) * 3 + (col // 3)

        #print(f"\nFinding value for i = {row}, j = {col}\n")
        #for line in board:
        #    print(line)

        for cell in "123456789":
            if cell in row_visited[row] or cell in col_visited[col] or cell in block_visited[block]:
                continue
            board[row][col] = cell
            row_visited[row].add(cell)
            col_visited[col].add(cell)
            block_visited[block].add(cell)
            if solve():
                return True
            row_visited[row].discard(cell)
            col_visited[col].discard(cell)
            block_visited[block].discard(cell)
            board[row][col] = "."

        return False

    solve()


def findEmptyCell(board: List[List[str]]) -> Optional[List[int]]:
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return [i, j]
    return None


#board = [["5","3",".",".","7",".",".",".","."],
#         ["6",".",".","1","9","5",".",".","."],
#         [".","9","8",".",".",".",".","6","."],
#         ["8",".",".",".","6",".",".",".","3"],
#         ["4",".",".","8",".","3",".",".","1"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".","6",".",".",".",".","2","8","."],
#         [".",".",".","4","1","9",".",".","5"],
#         [".",".",".",".","8",".",".","7","9"]]
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
solveSudoku(board)

print(board)
