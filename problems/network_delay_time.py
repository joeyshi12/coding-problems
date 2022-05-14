# https://leetcode.com/problems/network-delay-time/

import unittest
from typing import List
from collections import deque


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = {u: [] for u in range(1, n + 1)}
    for (u, v, w) in times:
        graph[u].append((v, w))

    delays = {k: 0}
    queue = deque([k])
    while queue:
        node = queue.popleft()
        for (v, w) in graph[node]:
            if v not in delays or delays[v] > delays[node] + w:
                delays[v] = delays[node] + w
                queue.append(v)

    return -1 if len(delays) < n else max(delay for delay in delays.values())


class TestNetworkDelayTime(unittest.TestCase):
    TEST_DATA = [
        (([[1, 2, 1]], 2, 2), -1),
        (([[1, 2, 1]], 2, 1), 1),
        (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
    ]

    def test_network_delay_time(self):
        for (times, n, k), expected in self.TEST_DATA:
            result = network_delay_time(times, n, k)
            print(f"{times, n, k} -> {result}")
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
