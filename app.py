#!/usr/bin/python3

# WRONG 1 pkxurafvhmebdtlzoqsjwcgiyn

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
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        u = yy % 100
        r = yy // 100
        a = (dd + ((13 * (mm + 1)) // 5) + u + (u // 4) + (r // 4) - 2 * r + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][a])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        