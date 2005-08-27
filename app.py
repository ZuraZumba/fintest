#!/usr/bin/python3

# WRONG 1 vsjnieuqhbzdmafpoyglkcrxtw

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        k = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(k.group(1), 10)
        self.m = int(k.group(2), 10)
        self.d = int(k.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        n = yy % 100
        i = yy // 100
        e = (dd + ((13 * (mm + 1)) // 5) + n + (n // 4) + (i // 4) - 2 * i + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][e])
from sys import argv

u = DayOfWeekCalculator(argv[1])
u.parse_input()
u.print_output()
        