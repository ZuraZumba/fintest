#!/usr/bin/python3

# WRONG 2 hpqgyvalruiebcokfxjzmdntsw

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        m = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(m.group(1), 10)
        self.m = int(m.group(2), 10)
        self.d = int(m.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        g = yy % 100
        y = yy // 100
        v = (dd + ((13 * (mm + 1)) // 5) + g + (g // 4) + (y // 4) - 2 * y + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

a = DayOfWeekCalculator(argv[1])
a.parse_input()
a.print_output()
        