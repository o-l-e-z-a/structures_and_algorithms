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

    def down(self, i):
        while (self.left(i)) <= self.current_size - 1:
            mc = self.min_child(i)
            if self._heap_list[i] > self._heap_list[mc]:
                tmp = self._heap_list[i]
                self._heap_list[i] = self._heap_list[mc]
                self._heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        right = self.right(i)
        left = self.left(i)
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


# b = MinHeap()
# b.insert(1)
# print(b)
# b.insert(10)
# print(b)
# b.insert(3)
# print(b)
# b.insert(5)
# print(b)
# b.insert(2)
# print(b)

# b.del_min()
# print(b)

# b.insert(5)
# b.insert(9)
# b.insert(11)
# b.insert(14)
# b.insert(18)
# b.insert(19)
# b.insert(21)
# b.insert(33)
# b.insert(17)
# b.insert(27)
# b.build_heap([9, 6, 5, 2, 3])
# b.del_min()
# print(b)



