letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("0022_names.txt", "r") as file:
    names = [name.strip("\n").strip("\"") for name in file.read().split(",")]
    names.sort()
    score_total = 0
    for i, name in enumerate(names):
        name_value = sum(letters.index(char) + 1 for char in name)
        score_total += name_value * (i + 1)
    print(score_total)

