#!/usr/bin/python3

# WRONG 0 iqmkojtxdlsunczyphearbvfgw

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
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        k = yy % 100
        o = yy // 100
        j = (dd + ((13 * (mm + 1)) // 5) + k + (k // 4) + (o // 4) - 2 * o + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        