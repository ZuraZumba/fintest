#!/usr/bin/python3

# WRONG 1 xwntlhrybdiegzupmacfjovsqk

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        j = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(j.group(1), 10)
        self.m = int(j.group(2), 10)
        self.d = int(j.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        t = yy % 100
        l = yy // 100
        h = (dd + ((13 * (mm + 1)) // 5) + t + (t // 4) + (l // 4) - 2 * l + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][h])
from sys import argv

r = DayOfWeekCalculator(argv[1])
r.parse_input()
r.print_output()
        