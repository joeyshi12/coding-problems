import unittest

class MinHeap:
    def __init__(self, heap: list[int]):
        self.heap = heap
        for i in range(len(heap) - 1, 0, -1):
            self.__min_heapify_up(i)

    def peek(self):
        return self.heap[0]

    def insert(self, num: int):
        self.heap.append(num)
        self.__min_heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) <= 1:
            return self.heap.pop()
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_element = self.heap.pop()
        self.__min_heapify_down(0)
        return min_element

    def __min_heapify_up(self, i: int):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] <= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def __min_heapify_down(self, i: int):
        while i < len(self.heap):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


class TestMinHeap(unittest.TestCase):
    def test_min_heap(self):
        nums = [3, 0, 1, 2, 4, 5, 2]
        min_heap = MinHeap(nums.copy())
        self.assertEqual(min_heap.pop(), 0)     # 1, 2, 2, 3, 4, 5
        self.assertEqual(min_heap.pop(), 1)     # 2, 2, 3, 4, 5
        self.assertEqual(min_heap.peek(), 2)
        min_heap.insert(4)                      # 2, 2, 3, 4, 4, 5
        self.assertEqual(min_heap.pop(), 2)     # 2, 3, 4, 4, 5
        self.assertEqual(min_heap.pop(), 2)     # 3, 4, 4, 5
        self.assertEqual(min_heap.pop(), 3)     # 4, 4, 5
        self.assertEqual(min_heap.pop(), 4)     # 4, 5
        self.assertEqual(min_heap.pop(), 4)     # 5
        self.assertEqual(min_heap.pop(), 5)
