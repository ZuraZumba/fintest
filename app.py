#!/usr/bin/python3

# RIGHT 0 ruvmqpfhnlxgcawskodtzbjiey

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        z = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(z.group(1), 10)
        self.m = int(z.group(2), 10)
        self.d = int(z.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        m = yy % 100
        q = yy // 100
        p = (dd + ((13 * (mm + 1)) // 5) + m + (m // 4) + (q // 4) - 2 * q + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][p])
from sys import argv

s = DayOfWeekCalculator(argv[1])
s.parse_input()
s.print_output()
        