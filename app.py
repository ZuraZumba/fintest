#!/usr/bin/python3

# WRONG 5 ysrkoipmaflneqxbdzjwvtugch

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        v = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(v.group(1), 10)
        self.m = int(v.group(2), 10)
        self.d = int(v.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        k = yy % 100
        o = yy // 100
        i = (dd + ((13 * mm) // 5) + k + (k // 4) + (o // 4) - 2 * o + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i])
from sys import argv

p = DayOfWeekCalculator(argv[1])
p.parse_input()
p.print_output()
        