#!/usr/bin/python3

# WRONG 1 zgjqtvscmhbpoxenrilyukwafd

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        u = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(u.group(1), 10)
        self.m = int(u.group(2), 10)
        self.d = int(u.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        q = yy % 100
        t = yy // 100
        v = (dd + ((13 * (mm + 1)) // 5) + q + (q // 4) + (t // 4) - 2 * t + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

s = DayOfWeekCalculator(argv[1])
s.parse_input()
s.print_output()
        