letters = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
triangle_numbers = [-1]


def is_triangle_number(num: int) -> bool:
    while triangle_numbers[-1] < num:
        n = len(triangle_numbers)
        triangle_numbers.append(n * (n + 1) // 2)

    return num in triangle_numbers


with open("0042_words.txt", "r") as file:
    count = 0
    words = [word.strip("\n").strip("\"") for word in file.read().split(",")]
    for word in words:
        word_value = sum(letters.index(char) for char in word)
        if is_triangle_number(word_value):
            print(word)
            count += 1
    print(count)
