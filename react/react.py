class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._observers = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for cb in self._observers:
            cb()

    def bind_to(self, callback):
        self._observers.append(callback)

    def __add__(self, other):
        return self._value + other

    def __sub__(self, other):
        return self._value - other

    def __mul__(self, other):
        return self._value * other

    def __lt__(self, other):
        return self._value < other


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.value = compute_function(inputs)
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []

        for i in inputs:
            i.bind_to(self.input_updated)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        try:
            self.callbacks.remove(callback)
        except ValueError:
            pass

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        other_value = 0
        if type(other) is int:
            other_value = other
        else:
            other_value = other.value
        return self.value - other_value

    def __mul__(self, other):
        return self.value * other.value

    def input_updated(self):
        result = self.compute_function(self.inputs)
        if result == self.value:
            return
        self.value = result
        for cb in self.callbacks:
            cb(self.value)

    def bind_to(self, value):
        for i in self.inputs:
            i.bind_to(value)
