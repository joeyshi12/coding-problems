# https://leetcode.com/problems/pascals-triangle-ii/submissions/

from typing import List

def get_row(row_index: int) -> List[int]:
    row = [1] * (row_index + 1)
    i = 1
    j = row_index
    top = j
    bot = i
    for i in range(1, (row_index + 1) // 2 + 1):
        row[i] = row[-1-i] = top // bot
        i += 1
        j -= 1
        top *= j
        bot *= i
    return row

# TODO: add tests
