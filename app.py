#!/usr/bin/python3

# WRONG 5 rtjyduaxvhibkcqwzfonlgesmp

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        l = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(l.group(1), 10)
        self.m = int(l.group(2), 10)
        self.d = int(l.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        y = yy % 100
        d = yy // 100
        u = (dd + ((13 * mm) // 5) + y + (y // 4) + (d // 4) - 2 * d + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

a = DayOfWeekCalculator(argv[1])
a.parse_input()
a.print_output()
        