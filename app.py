#!/usr/bin/python3

# WRONG 3 rgaloxeifzmnkdqjsuwtcbpvhy

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
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        l = yy % 100
        o = yy // 100
        x = (dd + ((13 * (mm + 1)) // 5) + l + (l // 4) + (o // 4) - 2 * o + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])
from sys import argv

e = DayOfWeekCalculator(argv[1])
e.parse_input()
e.print_output()
        