#!/usr/bin/python3

# RIGHT 0 csfehtwvbikaxpdujoylgqzmnr

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        g = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(g.group(1), 10)
        self.m = int(g.group(2), 10)
        self.d = int(g.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        e = yy % 100
        h = yy // 100
        t = (dd + ((13 * (mm + 1)) // 5) + e + (e // 4) + (h // 4) - 2 * h + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][t])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        