#!/usr/bin/python3

# WRONG 0 vejrxqfguonwsblzmdaichktpy

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        c = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(c.group(1), 10)
        self.m = int(c.group(2), 10)
        self.d = int(c.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        r = yy % 100
        x = yy // 100
        q = (dd + ((13 * (mm + 1)) // 5) + r + (r // 4) + (x // 4) - 2 * x + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        