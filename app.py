#!/usr/bin/python3

# WRONG 1 kgwtdbuofnmahspxilcqvrzjye

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
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        t = yy % 100
        d = yy // 100
        b = (dd + ((13 * (mm + 1)) // 5) + t + (t // 4) + (d // 4) - 2 * d + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][b])
from sys import argv

u = DayOfWeekCalculator(argv[1])
u.parse_input()
u.print_output()
        