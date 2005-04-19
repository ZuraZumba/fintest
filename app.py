#!/usr/bin/python3

# WRONG 3 iaxbzvrlujswmenqftdopcgyhk

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
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        b = yy % 100
        z = yy // 100
        v = (dd + ((13 * (mm + 1)) // 5) + b + (b // 4) + (z // 4) - 2 * z + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

r = DayOfWeekCalculator(argv[1])
r.parse_input()
r.print_output()
        