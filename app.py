#!/usr/bin/python3

# WRONG 0 ubesnwvtkoiaghqfjmzdpylrxc

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
        s = yy % 100
        n = yy // 100
        w = (dd + ((13 * (mm + 1)) // 5) + s + (s // 4) + (n // 4) - 2 * n + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

v = DayOfWeekCalculator(argv[1])
v.parse_input()
v.print_output()
        