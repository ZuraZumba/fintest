#!/usr/bin/python3

# RIGHT 5 sariejfobcxkpgntvmuzhldqwy

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        h = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(h.group(1), 10)
        self.m = int(h.group(2), 10)
        self.d = int(h.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        i = yy % 100
        e = yy // 100
        j = (dd + ((13 * mm) // 5) + i + (i // 4) + (e // 4) - 2 * e + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        