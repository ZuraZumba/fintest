#!/usr/bin/python3

# WRONG 4 yojgbqfdrwmvtnkexzhsluciap

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        l = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(l.group(1), 10)
        self.m = int(l.group(2), 10)
        self.d = int(l.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        g = yy % 100
        b = yy // 100
        q = (dd + ((13 * mm) // 5) + g + (g // 4) + (b // 4) - 2 * b + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        