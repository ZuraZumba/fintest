#!/usr/bin/python3

# WRONG 3 exhwvoysclndztbrqgukamjpfi

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        a = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(a.group(1), 10)
        self.m = int(a.group(2), 10)
        self.d = int(a.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        w = yy % 100
        v = yy // 100
        o = (dd + ((13 * (mm + 1)) // 5) + w + (w // 4) + (v // 4) - 2 * v + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][o])
from sys import argv

y = DayOfWeekCalculator(argv[1])
y.parse_input()
y.print_output()
        