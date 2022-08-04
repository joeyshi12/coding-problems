n = 2
prev = 1
curr = 1
while curr < 10 ** 999:
    prev, curr = curr, prev + curr
    n += 1

print(f"n = {n}")
print(f"Fibonacci number: {curr}")
