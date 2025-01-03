def main():
    with open("./p013_large_numbers.txt", encoding="utf-8") as f:
        nums = [int(num_str) for num_str in f.read().split()]
        print(str(sum(nums))[:10])


if __name__ == '__main__':
    main()
