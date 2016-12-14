import argparse
import logging
import sys

from pyfuck import interpreter


def parse_args():
    parser = argparse.ArgumentParser(description='PyFuck - Brainfuck interpreter')
    parser.add_argument('--file', '-f', action='store',
                        help='File with the Brainfuck code. If not specified code will be read from STDIN.')
    parser.add_argument('--debug', '-d', action='store_true',
                        help='Print all debug log on stderr.')

    return parser.parse_args()


def main():
    args = parse_args()
    if args.file:
        with open(args.file) as file:
            code = file.read()
    else:
        code = sys.stdin.read()

    if args.debug:
        interpreter.logger.setLevel(logging.DEBUG)
        interpreter.logger.addHandler(logging.StreamHandler(stream=sys.stderr))

    interpreter.Interpreter(code).run()


main()
