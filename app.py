#!/usr/bin/python3

# RIGHT 4 qidpxkfmtjwcahogbeulyzvnrs

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        y = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(y.group(1), 10)
        self.m = int(y.group(2), 10)
        self.d = int(y.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        p = yy % 100
        x = yy // 100
        k = (dd + ((13 * mm) // 5) + p + (p // 4) + (x // 4) - 2 * x + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][k])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        