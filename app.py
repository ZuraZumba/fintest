#!/usr/bin/python3

# WRONG 3 qabixlyjzvmswofgpntchkdreu

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        h = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(h.group(1), 10)
        self.m = int(h.group(2), 10)
        self.d = int(h.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        i = yy % 100
        x = yy // 100
        l = (dd + ((13 * (mm + 1)) // 5) + i + (i // 4) + (x // 4) - 2 * x + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][l])
from sys import argv

y = DayOfWeekCalculator(argv[1])
y.parse_input()
y.print_output()
        