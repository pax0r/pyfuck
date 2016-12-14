import logging

from pyfuck.getch import getch
from pyfuck.memory import Memory

logger = logging.getLogger(__name__)


class Interpreter(object):
    def __init__(self, code):
        self._code = str(code)
        self._code_position = 0
        self._position_stack = []
        self._vm = Memory()
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
        logger.debug('Bracket open')
        if not self._vm.get_cell():
            logger.debug('Jumping to close')
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
            logger.debug('Steping into bracket')
            self._position_stack.append(self._code_position)

    def _handle_bracket_close(self):
        if self._position_stack:
            logger.debug('Jumping to bracket open')
            self._code_position = self._position_stack.pop() - 1
        else:
            raise SyntaxError('No opening bracket!')

    def _print_character(self):
        print(chr(self._vm.get_cell()), end="")

    def _read_character(self):
        logger.debug('Reading character...')
        c = ord(getch())
        self._vm.set_cell(c)
        logger.debug('Read %s', c)

    def _noop(self):
        logger.debug('noop')

    def run(self):
        while self._code_position < len(self._code):
            c = self._code[self._code_position]
            self._code_map.get(c, self._noop)()
            self._code_position += 1
