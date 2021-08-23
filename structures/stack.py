from structures.base import BaseQueue


class Stack(BaseQueue):

    def push(self, value):
        self._list.insert(0, value)
