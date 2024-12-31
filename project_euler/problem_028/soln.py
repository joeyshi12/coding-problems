result = 1
i = 1
for gap in range(2, 1001, 2):
    for j in range(1, 5):
        result += i + j * gap
    i = i + 4 * gap

print(result)
