#!/usr/bin/python3

# WRONG 1 ndsaxqzkhmucfjlgeyvworbtpi

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        o = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(o.group(1), 10)
        self.m = int(o.group(2), 10)
        self.d = int(o.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        a = yy % 100
        x = yy // 100
        q = (dd + ((13 * (mm + 1)) // 5) + a + (a // 4) + (x // 4) - 2 * x + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

z = DayOfWeekCalculator(argv[1])
z.parse_input()
z.print_output()
        