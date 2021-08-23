class PriorityQueue:

    def push(self, key, value):
        pass

    def pop(self):
        pass

    def get(self):
        pass

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

