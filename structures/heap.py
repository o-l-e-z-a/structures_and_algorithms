class MinHeap:
    def __init__(self):
        self._heap_list = []
        self.current_size = 0

    def insert(self, value):
        self._heap_list.append(value)
        self.current_size = self.current_size + 1
        self.up(self.current_size - 1)

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left(index):
        return 2 * index + 1

    @staticmethod
    def right(index):
        return 2 * index + 2

    def up(self, index):
        parent = self.parent(index)
        while parent >= 0:
            if self._heap_list[parent] > self._heap_list[index]:
                self._heap_list[parent], self._heap_list[index] = self._heap_list[index], self._heap_list[parent]
                parent = self.parent(parent)
            else:
                break

    def down(self, index):
        while (self.left(index)) <= self.current_size - 1:
            min_child = self.min_child(index)
            if self._heap_list[index] > self._heap_list[min_child]:
                self._heap_list[index], self._heap_list[min_child] = self._heap_list[min_child], self._heap_list[index]
            index = min_child

    def min_child(self, index):
        right = self.right(index)
        left = self.left(index)
        if right > self.current_size - 1:
            return left
        else:
            if self._heap_list[left] < self._heap_list[right]:
                return left
            else:
                return right

    def del_min(self):
        result = self._heap_list[0]
        self._heap_list[0] = self._heap_list[self.current_size - 1]
        self.current_size -= 1
        self._heap_list.pop()
        self.down(0)
        return result

    def build_heap(self, arr):
        arr = list(arr)
        i = self.parent(len(arr))
        self.current_size = len(arr)
        self._heap_list = arr
        while i >= 0:
            self.down(i)
            i = i - 1

    def get_min(self):
        return self._heap_list[0]

    def __str__(self):
        return ' '.join([repr(x) for x in self._heap_list])

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join([repr(x) for x in self._heap_list])})'

    def __len__(self):
        return self.current_size

    def __eq__(self, other):
        return self._heap_list == list(other)
