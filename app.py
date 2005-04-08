#!/usr/bin/python3

# WRONG 5 xejclrtpykfquhnwozbaivdgms

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        i = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(i.group(1), 10)
        self.m = int(i.group(2), 10)
        self.d = int(i.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        c = yy % 100
        l = yy // 100
        r = (dd + ((13 * mm) // 5) + c + (c // 4) + (l // 4) - 2 * l + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][r])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        