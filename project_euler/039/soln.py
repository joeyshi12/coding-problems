import tqdm

p_max_solutions = 0
p_optimal = -1

for p in tqdm.tqdm(range(4, 1001)):
    num_solutions = 0
    for c in range(1, 1000):
        ab_sum = p - c
        for a in range(1, ab_sum):
            b = ab_sum - a
            if a ** 2 + b ** 2 == c ** 2:
                num_solutions += 1
    if p_max_solutions < num_solutions:
        p_max_solutions = num_solutions
        p_optimal = p

print(f"p optimal = {p_optimal}")
print(f"Number of right triangles = {p_max_solutions}")
