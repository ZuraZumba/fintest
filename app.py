#!/usr/bin/python3

# WRONG 1 qnzkxjgwylaeophsbmvudftcri

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
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        k = yy % 100
        x = yy // 100
        j = (dd + ((13 * (mm + 1)) // 5) + k + (k // 4) + (x // 4) - 2 * x + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

g = DayOfWeekCalculator(argv[1])
g.parse_input()
g.print_output()
        