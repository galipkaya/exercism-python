class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    def __str__(self):
        return self._value

    def __repr__(self):
        return str(self._value)


class LinkedList:
    def __init__(self, values=[]):
        current = None
        for v in values:
            node = Node(v, current)
            current = node
        self._head = current

    def __len__(self):
        if not self._head:
            return 0
        length = 0
        next_node = self._head
        while next_node:
            next_node = next_node.next()
            length += 1
        return length

    def head(self):
        if not self._head:
            raise EmptyListException("empty")
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)

    def pop(self):
        if self._head:
            node = self._head
            self._head = self._head.next()
            return node.value()
        else:
            raise EmptyListException("empty")

    def reversed(self):
        if not self._head:
            return self
        
        node = self._head
        previous = None
        while node.next():
            tmp = node.next()
            node.set_next(previous)
            previous = node
            node = tmp
        node.set_next(previous)
        self._head = node

        return self

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next()


class EmptyListException(Exception):
    pass
