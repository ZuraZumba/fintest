#!/usr/bin/python3

# WRONG 1 pakvoqcrudywxieblghjzfmnts

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        z = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(z.group(1), 10)
        self.m = int(z.group(2), 10)
        self.d = int(z.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        v = yy % 100
        o = yy // 100
        q = (dd + ((13 * (mm + 1)) // 5) + v + (v // 4) + (o // 4) - 2 * o + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        