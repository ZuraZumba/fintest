#!/usr/bin/python3

# WRONG 4 qgzlvjdfypmctbrhnakixsoewu

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        x = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(x.group(1), 10)
        self.m = int(x.group(2), 10)
        self.d = int(x.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        l = yy % 100
        v = yy // 100
        j = (dd + ((13 * mm) // 5) + l + (l // 4) + (v // 4) - 2 * v + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

d = DayOfWeekCalculator(argv[1])
d.parse_input()
d.print_output()
        