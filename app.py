#!/usr/bin/python3

# WRONG 3 mpnebvxwgrqahckyzotfdjsuli

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        d = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(d.group(1), 10)
        self.m = int(d.group(2), 10)
        self.d = int(d.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        e = yy % 100
        b = yy // 100
        v = (dd + ((13 * (mm + 1)) // 5) + e + (e // 4) + (b // 4) - 2 * b + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        