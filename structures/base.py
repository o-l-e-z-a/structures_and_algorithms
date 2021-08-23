import abc


class BaseQueue(abc.ABC):

    def __init__(self):
        self._list = []

    @abc.abstractmethod
    def push(self, value):
        """ Добавление элемента """

    def pop(self):
        if not self.is_empty():
            return self._list.pop(0)

    def get(self):
        if not self.is_empty():
            return self._list[0]

    def clear(self):
        self._list = []

    def is_empty(self):
        return self._list == []

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return ' '.join([repr(x) for x in self._list])

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join([repr(x) for x in self._list])})'

    def __eq__(self, other):
        return self._list == list(other)
