#!/usr/bin/python3

# WRONG 1 aojhxdvymkurpgstlbwfenczqi

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        e = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(e.group(1), 10)
        self.m = int(e.group(2), 10)
        self.d = int(e.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        h = yy % 100
        x = yy // 100
        d = (dd + ((13 * (mm + 1)) // 5) + h + (h // 4) + (x // 4) - 2 * x + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][d])
from sys import argv

v = DayOfWeekCalculator(argv[1])
v.parse_input()
v.print_output()
        