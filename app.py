#!/usr/bin/python3

# WRONG 1 dqsebyrjhwomnauzgplxfiktvc

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
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        e = yy % 100
        b = yy // 100
        y = (dd + ((13 * (mm + 1)) // 5) + e + (e // 4) + (b // 4) - 2 * b + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][y])
from sys import argv

r = DayOfWeekCalculator(argv[1])
r.parse_input()
r.print_output()
        