#!/usr/bin/python3

# WRONG 2 qeapoyxkndfcwghstmubrvzlji

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        r = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(r.group(1), 10)
        self.m = int(r.group(2), 10)
        self.d = int(r.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        p = yy % 100
        o = yy // 100
        y = (dd + ((13 * (mm + 1)) // 5) + p + (p // 4) + (o // 4) - 2 * o + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][y])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        