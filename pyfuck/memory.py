class Memory(object):
    def __init__(self):
        self._memory = [0]
        self._position = 0

    def increment_position(self):
        self._position += 1
        if len(self._memory) <= self._position:
            self._memory.append(0)

    def decrement_position(self):
        self._position -= 1

    def increment_cell(self):
        self._memory[self._position] += 1

    def decrement_cell(self):
        self._memory[self._position] -= 1

    def set_cell(self, value):
        self._memory[self._position] = value

    def get_cell(self):
        return self._memory[self._position]
