#!/usr/bin/python3

# WRONG 0 utbrepihjqfmglskycnovdzxwa

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        v = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(v.group(1), 10)
        self.m = int(v.group(2), 10)
        self.d = int(v.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        r = yy % 100
        e = yy // 100
        p = (dd + ((13 * (mm + 1)) // 5) + r + (r // 4) + (e // 4) - 2 * e + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][p])
from sys import argv

i = DayOfWeekCalculator(argv[1])
i.parse_input()
i.print_output()
        