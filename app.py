#!/usr/bin/python3

# WRONG 5 mczjsdnelwukftrqygovbiphax

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
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        j = yy % 100
        s = yy // 100
        d = (dd + ((13 * mm) // 5) + j + (j // 4) + (s // 4) - 2 * s + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][d])
from sys import argv

n = DayOfWeekCalculator(argv[1])
n.parse_input()
n.print_output()
        