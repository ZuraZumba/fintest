#!/usr/bin/python3

# WRONG 2 uldqobkmjxihrefzypsngvwcta

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        g = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(g.group(1), 10)
        self.m = int(g.group(2), 10)
        self.d = int(g.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        q = yy % 100
        o = yy // 100
        b = (dd + ((13 * (mm + 1)) // 5) + q + (q // 4) + (o // 4) - 2 * o + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][b])
from sys import argv

k = DayOfWeekCalculator(argv[1])
k.parse_input()
k.print_output()
        