import unittest

from structures.heap import MinHeap
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
