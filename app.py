#!/usr/bin/python3

# WRONG 2 cetrhjsqvdamgwufpoiknblyzx

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        n = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(n.group(1), 10)
        self.m = int(n.group(2), 10)
        self.d = int(n.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        r = yy % 100
        h = yy // 100
        j = (dd + ((13 * (mm + 1)) // 5) + r + (r // 4) + (h // 4) - 2 * h + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

s = DayOfWeekCalculator(argv[1])
s.parse_input()
s.print_output()
        