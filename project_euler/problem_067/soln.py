import problem_018


def main():
    with open("./p067_triangle.txt", encoding="utf-8") as f:
        data = []
        for line in f:
            data.append([int(num) for num in line.split()])
        max_path_sum = problem_018.maximum_path_sum(data)
        print(f"Max path sum = {max_path_sum}")


if __name__ == '__main__':
    main()
