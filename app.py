#!/usr/bin/python3

# WRONG 5 fovupdcrgxaitwkjlbshnymezq

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        n = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(n.group(1), 10)
        self.m = int(n.group(2), 10)
        self.d = int(n.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        u = yy % 100
        p = yy // 100
        d = (dd + ((13 * mm) // 5) + u + (u // 4) + (p // 4) - 2 * p + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][d])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        