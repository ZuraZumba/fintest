#!/usr/bin/python3

# RIGHT 3 fyzdnumhwgatibxlrjecvqoksp

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
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        d = yy % 100
        n = yy // 100
        u = (dd + ((13 * (mm + 1)) // 5) + d + (d // 4) + (n // 4) - 2 * n + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

m = DayOfWeekCalculator(argv[1])
m.parse_input()
m.print_output()
        