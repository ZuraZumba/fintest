#!/usr/bin/python3

# RIGHT 1 qpjkntvluihsbocwmxfdrgzeya

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
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        k = yy % 100
        n = yy // 100
        t = (dd + ((13 * (mm + 1)) // 5) + k + (k // 4) + (n // 4) - 2 * n + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][t])
from sys import argv

v = DayOfWeekCalculator(argv[1])
v.parse_input()
v.print_output()
        