"""
Given a grid of robot positions, indicate if it is a valid time series
for the number of robots specified if robots can only travel
up to 1 index further than their position 1 step before

Input format: an array of arrays, of which each index can be 0 or 1.
An index corresponds to the physical location which is either occupied by a robot (1) or empty (0)

Grid: [[1,0,0,1],[0,1,1,0]]
is valid since 0 -> 1 and 3 -> 2 are 1 step forward and back

Grid: [[1,0,0,0,1],[1,0,1,0,0]]
is not valid since the second robot at 4 doesn't have a valid step to go to
"""

def is_valid_time_series(grid: list[list[int]]) -> bool:
    n = len(grid[0])
    for row_index in range(1, len(grid)):
        row1 = grid[row_index - 1]
        row2 = grid[row_index]
        if sum(row1) != sum(row2):
            return False
        i, j = 0, 0
        while i < n or j < n:
            if i < n and j < n and row1[i] == 1 and row2[j] == 1:
                if abs(i - j) > 1:
                    return False
                i += 1
                j += 1
                continue
            if i < n and row1[i] == 0:
                i += 1
            if j < n and row2[j] == 0:
                j += 1
    return True

grid1 = [[1,0,0,1],[0,1,1,0]]
grid2 = [[1,0,0,0,1],[1,0,1,0,0]]
print(is_valid_time_series(grid1))
print(is_valid_time_series(grid2))
