#!/usr/bin/python3

# WRONG 3 jtxawbzsoqmgdknryechpufilv

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        p = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(p.group(1), 10)
        self.m = int(p.group(2), 10)
        self.d = int(p.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        a = yy % 100
        w = yy // 100
        b = (dd + ((13 * (mm + 1)) // 5) + a + (a // 4) + (w // 4) - 2 * w + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][b])
from sys import argv

z = DayOfWeekCalculator(argv[1])
z.parse_input()
z.print_output()
        