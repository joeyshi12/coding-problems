import math


sum_digits = sum(int(digit) for digit in str(math.factorial(100)))
print(f"Digit sum of 100! = {sum_digits}")
