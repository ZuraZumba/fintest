#!/usr/bin/python3

# RIGHT 0 tkfbmwgaevucjdqyilnsporzxh

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        p = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(p.group(1), 10)
        self.m = int(p.group(2), 10)
        self.d = int(p.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        b = yy % 100
        m = yy // 100
        w = (dd + ((13 * (mm + 1)) // 5) + b + (b // 4) + (m // 4) - 2 * m + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

g = DayOfWeekCalculator(argv[1])
g.parse_input()
g.print_output()
        