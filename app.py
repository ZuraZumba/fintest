#!/usr/bin/python3

# RIGHT 6 cgtukviloadsfpmynexqrzjwbh

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        r = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(r.group(1), 10)
        self.m = int(r.group(2), 10)
        self.d = int(r.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        u = yy % 100
        k = yy // 100
        v = (dd + ((13 * mm) // 5) + u + (u // 4) + (k // 4) - 2 * k + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

i = DayOfWeekCalculator(argv[1])
i.parse_input()
i.print_output()
        