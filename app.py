#!/usr/bin/python3

# WRONG 2 pzwnedmkbsltjviuxhyofaqgrc

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        f = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(f.group(1), 10)
        self.m = int(f.group(2), 10)
        self.d = int(f.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        n = yy % 100
        e = yy // 100
        d = (dd + ((13 * (mm + 1)) // 5) + n + (n // 4) + (e // 4) - 2 * e + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][d])
from sys import argv

m = DayOfWeekCalculator(argv[1])
m.parse_input()
m.print_output()
        