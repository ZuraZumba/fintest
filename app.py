#!/usr/bin/python3

# WRONG 2 oifxpmdgclzhykbqaejtvsnwur

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        v = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(v.group(1), 10)
        self.m = int(v.group(2), 10)
        self.d = int(v.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        x = yy % 100
        p = yy // 100
        m = (dd + ((13 * (mm + 1)) // 5) + x + (x // 4) + (p // 4) - 2 * p + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][m])
from sys import argv

d = DayOfWeekCalculator(argv[1])
d.parse_input()
d.print_output()
        