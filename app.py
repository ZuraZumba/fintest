#!/usr/bin/python3

# WRONG 6 xncmrwdsityoqflgjhzveubpka

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        e = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(e.group(1), 10)
        self.m = int(e.group(2), 10)
        self.d = int(e.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        m = yy % 100
        r = yy // 100
        w = (dd + ((13 * mm) // 5) + m + (m // 4) + (r // 4) - 2 * r + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

d = DayOfWeekCalculator(argv[1])
d.parse_input()
d.print_output()
        