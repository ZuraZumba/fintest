#!/usr/bin/python3

# RIGHT 2 hgrnsczdaxpktuvolmfieyqjbw

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        e = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(e.group(1), 10)
        self.m = int(e.group(2), 10)
        self.d = int(e.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        n = yy % 100
        s = yy // 100
        c = (dd + ((13 * (mm + 1)) // 5) + n + (n // 4) + (s // 4) - 2 * s + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][c])
from sys import argv

z = DayOfWeekCalculator(argv[1])
z.parse_input()
z.print_output()
        