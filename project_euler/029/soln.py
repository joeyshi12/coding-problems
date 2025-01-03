terms = set()
for a in range(2, 101):
    acc = a
    for _ in range(2, 101):
        acc *= a
        terms.add(acc)
print(len(terms))

