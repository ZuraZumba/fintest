#!/usr/bin/python3

# WRONG 2 pcfmzswtgeavquioynjdkbxrlh

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        k = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(k.group(1), 10)
        self.m = int(k.group(2), 10)
        self.d = int(k.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        m = yy % 100
        z = yy // 100
        s = (dd + ((13 * (mm + 1)) // 5) + m + (m // 4) + (z // 4) - 2 * z + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][s])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        