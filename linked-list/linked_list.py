class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.previous = previous

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.tail:
            new_node.previous = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def pop(self):
        return self.remove(self.tail)

    def unshift(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def shift(self):
        return self.remove(self.head)

    def remove(self, node):
        value = node.value

        if self.head == self.tail:
            self.tail.previous = None
            self.head.next = None

        if node == self.tail:
            self.tail.next = None
            self.tail = self.tail.previous
        else:
            self.head.previous = None
            self.head = self.head.next

        if not self.head:
            self.tail = None
        if not self.tail:
            self.head = None
        return value

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length

