#!/usr/bin/python3

# WRONG 6 gbxdnurcizolfkvmpsyhtejawq

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        t = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(t.group(1), 10)
        self.m = int(t.group(2), 10)
        self.d = int(t.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        d = yy % 100
        n = yy // 100
        u = (dd + ((13 * mm) // 5) + d + (d // 4) + (n // 4) - 2 * n + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

r = DayOfWeekCalculator(argv[1])
r.parse_input()
r.print_output()
        