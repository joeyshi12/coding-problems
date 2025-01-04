max_digit_sum = 0
for a in range(1, 101):
    num = 1
    for _ in range(1, 101):
        num *= a
        digit_sum = sum(int(c) for c in str(num))
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
print(max_digit_sum)
        
