#!/usr/bin/python3

# WRONG 7 etukynclovxamzgfrjhpdisbwq

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        d = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(d.group(1), 10)
        self.m = int(d.group(2), 10)
        self.d = int(d.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        k = yy % 100
        y = yy // 100
        n = (dd + ((13 * mm) // 5) + k + (k // 4) + (y // 4) - 2 * y + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][n])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        