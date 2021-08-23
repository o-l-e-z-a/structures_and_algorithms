import unittest

from structures.heap import MinHeap
from structures.priority_queue import PriorityMinQueue
from structures.queue import Queue
from structures.stack import Stack


class TestMinHeap(unittest.TestCase):
    def test_create_and_delete_1(self):
        arr = [1, 10, 3, 5, 2]
        heap_list = [1, 2, 3, 10, 5]
        heap_list_with_delete = [2, 5, 3, 10]
        b = MinHeap()
        for x in arr:
            b.insert(x)
        self.assertEqual(b, heap_list)
        b.del_min()
        self.assertEqual(b, heap_list_with_delete)

    def test_create_and_delete_2(self):
        arr = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
        heap_list_with_delete = [9, 14, 11, 17, 18, 19, 21, 33, 27]
        b = MinHeap()
        for x in arr:
            b.insert(x)
        b.del_min()
        self.assertEqual(b, heap_list_with_delete)

    def test_build_from_arr(self):
        b = MinHeap()
        b.build_heap([9, 6, 5, 2, 3])
        arr = [2, 3, 5, 6, 9]
        self.assertEqual(b, arr)


class TestPriorityMinQueue(unittest.TestCase):
    def test_create_and_delete_1(self):
        priorities = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
        values = [i * 10 for i in range(1, len(priorities) + 1)]
        heap_list_with_delete = [(20, 9), (40, 14), (30, 11), (90, 17), (50, 18), (60, 19), (70, 21), (80, 33), (100, 27)]
        b = PriorityMinQueue()
        for node in list(zip(values, priorities)):
            b.insert(*node)
        b.del_min()
        self.assertEqual(b, heap_list_with_delete)

    def test_create_and_delete_2(self):
        priorities = [1, 10, 3, 5, 2]
        values = [i*100 for i in range(1, len(priorities) + 1)]
        heap_list = [(100, 1), (500, 2), (300, 3), (200, 10), (400, 5)]
        heap_list_with_delete = [(500, 2), (400, 5), (300, 3), (200, 10)]
        b = PriorityMinQueue()
        for node in list(zip(values, priorities)):
            b.insert(*node)
        self.assertEqual(b, heap_list)
        b.del_min()
        self.assertEqual(b, heap_list_with_delete)

    def test_build_from_arr(self):
        priorities = [9, 6, 5, 2, 3]
        values = [i * 100 for i in range(1, len(priorities) + 1)]
        b = PriorityMinQueue()
        b.build_heap(list(zip(values, priorities)))
        arr = [(400, 2), (500, 3), (300, 5), (200, 6), (100, 9)]
        self.assertEqual(b, arr)


class TestQueue(unittest.TestCase):

    def test_queue(self):
        queue = Queue()
        queue.push(1)
        queue.push(5)
        queue.push(10)
        self.assertEqual(queue, [1, 5, 10])
        queue.pop()
        queue.pop()
        self.assertEqual(queue, [10])


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        stack.push(4)
        stack.push(5)
        stack.push(1)
        self.assertEqual(stack, [1, 5, 4])
        stack.pop()
        stack.pop()
        self.assertEqual(stack, [4])


if __name__ == '__main__':
    unittest.main()
