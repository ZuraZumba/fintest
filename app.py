#!/usr/bin/python3

# WRONG 2 iokjbstnpxervdlafczmhyqgwu

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        h = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(h.group(1), 10)
        self.m = int(h.group(2), 10)
        self.d = int(h.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        j = yy % 100
        b = yy // 100
        s = (dd + ((13 * (mm + 1)) // 5) + j + (j // 4) + (b // 4) - 2 * b + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][s])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        