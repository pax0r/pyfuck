from pyfuck.getch import getch
from pyfuck.vm import VirtualMachine


def _noop():
    pass


class Interpreter(object):
    def __init__(self, **kwargs):
        if 'file' in kwargs:
            # read program from file
            with open(kwargs['file']) as f:
                self._code = f.read()
        elif 'code' in kwargs:
            # read code from string in kwargs['code']
            self._code = kwargs['code']
        else:
            raise ValueError('You need to specify file or string with code!')
        self._code_position = 0
        self._position_stack = []
        self._vm = VirtualMachine()
        self._code_map = {
            '>': self._vm.increment_position,
            '<': self._vm.decrement_position,
            '+': self._vm.increment_cell,
            '-': self._vm.decrement_cell,
            '.': self._print_character,
            ',': self._read_character,
            '[': self._handle_bracket_open,
            ']': self._handle_bracket_close
        }

    def _handle_bracket_open(self):
        if not self._vm.get_cell():
            brackets = 1
            while self._code_position < len(self._code):
                self._code_position += 1
                if self._code[self._code_position] == '[':
                    brackets += 1
                elif self._code[self._code_position] == ']':
                    brackets -= 1
                if brackets == 0:
                    return
            raise SyntaxError('No closing bracket!')
        else:
            self._position_stack.append(self._code_position)

    def _handle_bracket_close(self):
        if self._position_stack:
            self._code_position = self._position_stack.pop() - 1
        else:
            raise SyntaxError('No opening bracket!')

    def _print_character(self):
        print(chr(self._vm.get_cell()), end="")

    def _read_character(self):
        c = getch()
        self._vm.set_cell(ord(c))

    def run(self):
        while self._code_position < len(self._code):
            c = self._code[self._code_position]
            self._code_map.get(c, _noop)()
            self._code_position += 1
