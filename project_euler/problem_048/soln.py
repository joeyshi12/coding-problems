mod_sum = 0
for i in range(1, 1001):
    mod_term = 1
    for _ in range(i):
        mod_term = mod_term * i
    mod_sum = mod_sum + mod_term
print(mod_sum % 10000000000)
