#!/usr/bin/python3

# WRONG 2 axvdkhelwqirgfymbtcnozjups

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
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        d = yy % 100
        k = yy // 100
        h = (dd + ((13 * (mm + 1)) // 5) + d + (d // 4) + (k // 4) - 2 * k + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][h])
from sys import argv

e = DayOfWeekCalculator(argv[1])
e.parse_input()
e.print_output()
        