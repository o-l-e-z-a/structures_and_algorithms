from structures.heap import MinHeap


class Node:

    def __init__(self, value, priority):
        self.info = value
        self.priority = priority

    def __repr__(self):
        return f'({self.info}, {self.priority})'

    def __eq__(self, other):
        if isinstance(other, Node):
            return (self.info, self.priority) == (other.info, other.priority)
        else:
            return (self.info, self.priority) == tuple(other)

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority


class PriorityMinQueue(MinHeap):

    def insert(self, value, priority):
        node = Node(value, priority)
        self._heap_list.append(node)
        self.current_size = self.current_size + 1
        self.up(self.current_size - 1)

    def build_heap(self, arr):
        arr = list(arr)
        for i in range(len(arr)):
            arr[i] = Node(*arr[i])
        super().build_heap(arr)


