#!/usr/bin/python3

# WRONG 7 pavmekqstrbljizfgudcwhxyno

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        w = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(w.group(1), 10)
        self.m = int(w.group(2), 10)
        self.d = int(w.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        m = yy % 100
        e = yy // 100
        k = (dd + ((13 * mm) // 5) + m + (m // 4) + (e // 4) - 2 * e + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][k])
from sys import argv

q = DayOfWeekCalculator(argv[1])
q.parse_input()
q.print_output()
        