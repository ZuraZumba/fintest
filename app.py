#!/usr/bin/python3

# WRONG 7 owtxhyljevmcgidsbkrfznuqpa

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        z = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(z.group(1), 10)
        self.m = int(z.group(2), 10)
        self.d = int(z.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        x = yy % 100
        h = yy // 100
        y = (dd + ((13 * mm) // 5) + x + (x // 4) + (h // 4) - 2 * h + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][y])
from sys import argv

l = DayOfWeekCalculator(argv[1])
l.parse_input()
l.print_output()
        