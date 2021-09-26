class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.first_index = 0
        self.last_index = 0

    def _increase_index(self, index):
        index += 1
        if index >= self.capacity:
            index = 0
        return index

    def read(self):
        if all([x is None for x in self.buffer]):
            raise BufferEmptyException("empty")
        data = self.buffer[self.first_index]
        self.buffer[self.first_index] = None
        self.first_index = self._increase_index(self.first_index)
        return data

    def _write(self, data):
        self.buffer[self.last_index] = data
        self.last_index = self._increase_index(self.last_index)

    def write(self, data):
        if all([x is not None for x in self.buffer]):
            raise BufferEmptyException("full")
        self._write(data)

    def overwrite(self, data):
        if self.buffer[self.last_index] is None:
            self._write(data)
        else:
            self._write(data)
            self.first_index = self._increase_index(self.first_index)

    def clear(self):
        self.__init__(self.capacity)
