def find_minimal_path_sum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    minimal_path_sums = [[0] * n for _ in range(n)]
    minimal_path_sums[0][0] = matrix[0][0]

    for i in range(1, n):
        minimal_path_sums[i][0] = minimal_path_sums[i - 1][0] + matrix[i][0]

    for j in range(1, n):
        minimal_path_sums[0][j] = minimal_path_sums[0][j - 1] + matrix[0][j]

    for i in range(1, n):
        for j in range(n - i):
            minimal_path_sums[i + j][i] = matrix[i + j][i] + min(
                minimal_path_sums[i + j - 1][i],
                minimal_path_sums[i + j][i - 1]
            )

        for j in range(n - i):
            minimal_path_sums[i][i + j] = matrix[i][i + j] + min(
                minimal_path_sums[i - 1][i + j],
                minimal_path_sums[i][i + j - 1]
            )

    return minimal_path_sums[-1][-1]


with open("0081_matrix.txt", "r") as file:
    matrix = []
    for line in file:
        matrix.append([int(num) for num in line.split(",")])
    print(find_minimal_path_sum(matrix))

