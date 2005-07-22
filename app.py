#!/usr/bin/python3

# WRONG 0 cezpwnsahkyuvdjblgiormtxfq

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        r = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(r.group(1), 10)
        self.m = int(r.group(2), 10)
        self.d = int(r.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        p = yy % 100
        w = yy // 100
        n = (dd + ((13 * (mm + 1)) // 5) + p + (p // 4) + (w // 4) - 2 * w + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][n])
from sys import argv

s = DayOfWeekCalculator(argv[1])
s.parse_input()
s.print_output()
        