#!/usr/bin/python3

# WRONG 0 vwsnbatrkfgdmjlpeqzuoyihcx

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
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        n = yy % 100
        b = yy // 100
        a = (dd + ((13 * (mm + 1)) // 5) + n + (n // 4) + (b // 4) - 2 * b + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][a])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        