#!/usr/bin/python3

# WRONG 5 emjhwtfxqvuzabciodprgnyksl

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        g = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(g.group(1), 10)
        self.m = int(g.group(2), 10)
        self.d = int(g.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        h = yy % 100
        w = yy // 100
        t = (dd + ((13 * mm) // 5) + h + (h // 4) + (w // 4) - 2 * w + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][t])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        