#!/usr/bin/python3

# WRONG 3 jegfvuzboisdlknacmwpqyhtxr

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        q = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(q.group(1), 10)
        self.m = int(q.group(2), 10)
        self.d = int(q.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        f = yy % 100
        v = yy // 100
        u = (dd + ((13 * (mm + 1)) // 5) + f + (f // 4) + (v // 4) - 2 * v + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

z = DayOfWeekCalculator(argv[1])
z.parse_input()
z.print_output()
        