#!/usr/bin/python3

# WRONG 2 rdzecpngyjbkmtwqvfhisloxua

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        s = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(s.group(1), 10)
        self.m = int(s.group(2), 10)
        self.d = int(s.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        e = yy % 100
        c = yy // 100
        p = (dd + ((13 * (mm + 1)) // 5) + e + (e // 4) + (c // 4) - 2 * c + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][p])
from sys import argv

n = DayOfWeekCalculator(argv[1])
n.parse_input()
n.print_output()
        