#!/usr/bin/python3

# WRONG 1 matousbnlxrfgpqdiceywhjvkz

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        w = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(w.group(1), 10)
        self.m = int(w.group(2), 10)
        self.d = int(w.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        o = yy % 100
        u = yy // 100
        s = (dd + ((13 * (mm + 1)) // 5) + o + (o // 4) + (u // 4) - 2 * u + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][s])
from sys import argv

b = DayOfWeekCalculator(argv[1])
b.parse_input()
b.print_output()
        