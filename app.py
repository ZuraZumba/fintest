#!/usr/bin/python3

# WRONG 3 flxhurtgwnsacvmjqoykbdzepi

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        b = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(b.group(1), 10)
        self.m = int(b.group(2), 10)
        self.d = int(b.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        h = yy % 100
        u = yy // 100
        r = (dd + ((13 * (mm + 1)) // 5) + h + (h // 4) + (u // 4) - 2 * u + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][r])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        