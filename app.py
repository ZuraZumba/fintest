#!/usr/bin/python3

# WRONG 3 qhlikstpbcmwgxevrjdynzafou

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        n = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(n.group(1), 10)
        self.m = int(n.group(2), 10)
        self.d = int(n.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        i = yy % 100
        k = yy // 100
        s = (dd + ((13 * (mm + 1)) // 5) + i + (i // 4) + (k // 4) - 2 * k + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][s])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        