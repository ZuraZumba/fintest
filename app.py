#!/usr/bin/python3

# WRONG 6 gyzvdqbaonskiwtprmxfhjeucl

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        h = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(h.group(1), 10)
        self.m = int(h.group(2), 10)
        self.d = int(h.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        v = yy % 100
        d = yy // 100
        q = (dd + ((13 * mm) // 5) + v + (v // 4) + (d // 4) - 2 * d + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

b = DayOfWeekCalculator(argv[1])
b.parse_input()
b.print_output()
        