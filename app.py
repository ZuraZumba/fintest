#!/usr/bin/python3

# WRONG 2 acstljfqorgxdikzpvywunebhm

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        u = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(u.group(1), 10)
        self.m = int(u.group(2), 10)
        self.d = int(u.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        t = yy % 100
        l = yy // 100
        j = (dd + ((13 * (mm + 1)) // 5) + t + (t // 4) + (l // 4) - 2 * l + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        