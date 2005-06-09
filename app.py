#!/usr/bin/python3

# WRONG 6 xnslpdhzjwbmvrtyogfciaeuqk

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
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        l = yy % 100
        p = yy // 100
        d = (dd + ((13 * mm) // 5) + l + (l // 4) + (p // 4) - 2 * p + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][d])
from sys import argv

h = DayOfWeekCalculator(argv[1])
h.parse_input()
h.print_output()
        