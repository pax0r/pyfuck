# PyFuck
Brainfuck interpreter written using Python3.
More on Brainfuck: https://en.wikipedia.org/wiki/Brainfuck

# Usage from bash
Run code from the file:

`bin/bf -f source_file`

Run code from stdin:
`cat source_file > bin/bf`

# Usage from python

```python
from pyfuck import Interpreter

source_code = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'

Interpreter(code=source_code).run()
```


# Implementation notes:
- Cells can store any int or long number (not only 8-bit chars)
- Number of cells is limited only by memory
- Reading cells using negative index is undefined (may wraps to the end of the allocated memory or raise IndexError) and may change in the future.
- It can print any UTF-8 character (not only ASCII). If number stored in cell is not UTF-8 it will raise ValueError on printing (but you can store them, just don't use `.` on them!)