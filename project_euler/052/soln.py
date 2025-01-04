def get_char_counts(val: str) -> dict[str, int]:
    char_counts = {}
    for c in val:
        char_counts[c] = char_counts.get(c, 0) + 1
    return char_counts


def is_valid(num: int) -> bool:
    char_counts_maps = [get_char_counts(str(num * i)) for i in range(1, 7)]
    for i in range(1, len(char_counts_maps)):
        if char_counts_maps[i] != char_counts_maps[0]:
            return False
    return True


for num in range(100000, 200000):
    if is_valid(num):
        print(num)
        break
