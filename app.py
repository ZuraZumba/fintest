#!/usr/bin/python3

# RIGHT 3 utqpjihoybvwkxrlzadgmsfcen

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        m = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(m.group(1), 10)
        self.m = int(m.group(2), 10)
        self.d = int(m.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        p = yy % 100
        j = yy // 100
        i = (dd + ((13 * (mm + 1)) // 5) + p + (p // 4) + (j // 4) - 2 * j + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i])
from sys import argv

h = DayOfWeekCalculator(argv[1])
h.parse_input()
h.print_output()
        