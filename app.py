#!/usr/bin/python3

# RIGHT 6 fbronwtvxqdulepajcgszymhki

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
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        o = yy % 100
        n = yy // 100
        w = (dd + ((13 * mm) // 5) + o + (o // 4) + (n // 4) - 2 * n + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        