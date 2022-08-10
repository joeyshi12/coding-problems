def num_lattice_paths(n: int) -> int:
    cache = {}

    def _num_lattice_paths(i: int, j: int) -> int:
        if i == n or j == n:
            return 1
        if (i, j) not in cache:
            count = 0
            for a, b in [(i + 1, j), (i, j + 1)]:
                if a <= n and b <= n:
                    count += _num_lattice_paths(a, b)
            cache[i, j] = count
        return cache[i, j]

    return _num_lattice_paths(0, 0)

num_paths = num_lattice_paths(20)
print(f"Number of lattice paths: {num_paths}")
