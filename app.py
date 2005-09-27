#!/usr/bin/python3

# WRONG 2 zapqnogvstmflydkjhxbiruwec

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        i = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(i.group(1), 10)
        self.m = int(i.group(2), 10)
        self.d = int(i.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        q = yy % 100
        n = yy // 100
        o = (dd + ((13 * (mm + 1)) // 5) + q + (q // 4) + (n // 4) - 2 * n + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][o])
from sys import argv

g = DayOfWeekCalculator(argv[1])
g.parse_input()
g.print_output()
        