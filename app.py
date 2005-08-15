#!/usr/bin/python3

# WRONG 5 zgdlheantufvimpywkxqjocbsr

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        j = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(j.group(1), 10)
        self.m = int(j.group(2), 10)
        self.d = int(j.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        l = yy % 100
        h = yy // 100
        e = (dd + ((13 * mm) // 5) + l + (l // 4) + (h // 4) - 2 * h + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][e])
from sys import argv

a = DayOfWeekCalculator(argv[1])
a.parse_input()
a.print_output()
        