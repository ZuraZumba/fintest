#!/usr/bin/python3

# WRONG 4 sniztvoyglfaqpuhmkjdwcerxb

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        w = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(w.group(1), 10)
        self.m = int(w.group(2), 10)
        self.d = int(w.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        z = yy % 100
        t = yy // 100
        v = (dd + ((13 * mm) // 5) + z + (z // 4) + (t // 4) - 2 * t + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

o = DayOfWeekCalculator(argv[1])
o.parse_input()
o.print_output()
        