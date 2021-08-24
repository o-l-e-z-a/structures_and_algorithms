class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_value = None

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class LinkedList:

    def __init__(self):
        self.head = None

    def contains(self, value):
        last_node = self.head
        while last_node:
            if value == last_node.cat:
                return True
            else:
                last_node = last_node.next_value
        return False

    def add_to_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_value:
            last_node = last_node.next_value
        last_node.next_value = new_node

    def add_to_start(self, value):
        new_node = Node(value)
        new_node.next_value = self.head
        self.head = new_node

    def remove(self, value):
        head = self.head

        if head is not None:
            if head.value == value:
                self.head = head.next_value
                head = None
                return
        while head is not None:
            if head.value == value:
                break
            last = head
            head = head.next_value
        if not head:
            return
        last.next_value = head.next_value
        head = None

    def get(self, index):
        last = self.head
        node_index = 0
        while node_index <= index:
            if node_index == index:
                return last.value
            node_index += 1
            last = last.next_value

    def __str__(self):
        string = ''
        node = self.head
        while node:
            string += f' {repr(node.value)}'
            node = node.next_value
        return string

    def __repr__(self):
        string = 'LinkedList'
        node = self.head
        while node:
            string += f' {repr(node.value)}'
            node = node.next_value
        return string
