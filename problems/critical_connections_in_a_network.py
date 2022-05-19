# https://leetcode.com/problems/critical-connections-in-a-network/
# https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

import unittest
from typing import List


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = [[] for _ in range(n)]
    for (a, b) in connections:
        graph[a].append(b)
        graph[b].append(a)

    connections = []
    __critical_connections(graph, 0, -1, 0, [n] * n, [False] * n, connections)
    return connections


def __critical_connections(graph: List[List[int]],
                           curr: int,
                           prev: int,
                           curr_rank: int,
                           lowest_ranks: List[int],
                           visited: List[bool],
                           connections: List[List[int]]) -> None:
    visited[curr] = True
    lowest_ranks[curr] = curr_rank
    for next_node in graph[curr]:
        if next_node == prev:
            continue
        if not visited[next_node]:
            __critical_connections(graph, next_node, curr, curr_rank + 1, lowest_ranks, visited, connections)
        lowest_ranks[curr] = min(lowest_ranks[curr], lowest_ranks[next_node])
        if lowest_ranks[curr] < lowest_ranks[next_node]:
            connections.append([curr, next_node])


class TestCriticalConnections(unittest.TestCase):
    TEST_DATA = [
        ((2, [[0, 1]]), [[0, 1]]),
        ((4, [[0, 1],[1, 2],[2, 0],[1, 3]]), [[1, 3]]),
        ((4, [[0, 1], [1, 2], [1, 3]]), [[0, 1], [1, 2], [1, 3]])
    ]

    def test_critical_connection(self):
        for (n, connections), expected in self.TEST_DATA:
            result = critical_connections(n, connections)
            print(f"{n, connections} -> {result}")
            for row in result:
                row.sort()
            for row in expected:
                row.sort()
            result.sort()
            expected.sort()
            self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
