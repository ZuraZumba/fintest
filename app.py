#!/usr/bin/python3

# RIGHT 2 rvzmgqlkpocuhfntsdxebwaijy

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        b = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(b.group(1), 10)
        self.m = int(b.group(2), 10)
        self.d = int(b.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        m = yy % 100
        g = yy // 100
        q = (dd + ((13 * (mm + 1)) // 5) + m + (m // 4) + (g // 4) - 2 * g + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

l = DayOfWeekCalculator(argv[1])
l.parse_input()
l.print_output()
        