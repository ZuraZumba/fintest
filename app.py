#!/usr/bin/python3

# WRONG 6 mloivhpagkquxejbsdryctfwzn

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        c = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(c.group(1), 10)
        self.m = int(c.group(2), 10)
        self.d = int(c.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        i = yy % 100
        v = yy // 100
        h = (dd + ((13 * mm) // 5) + i + (i // 4) + (v // 4) - 2 * v + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][h])
from sys import argv

p = DayOfWeekCalculator(argv[1])
p.parse_input()
p.print_output()
        