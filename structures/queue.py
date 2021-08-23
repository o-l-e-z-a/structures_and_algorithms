from structures.base import BaseQueue


class Queue(BaseQueue):

    def push(self, value):
        self._list.append(value)

