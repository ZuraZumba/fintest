#!/usr/bin/python3

# RIGHT 6 ibgeluqhonftwxvrmzdkpycjas

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        p = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(p.group(1), 10)
        self.m = int(p.group(2), 10)
        self.d = int(p.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        e = yy % 100
        l = yy // 100
        u = (dd + ((13 * mm) // 5) + e + (e // 4) + (l // 4) - 2 * l + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

q = DayOfWeekCalculator(argv[1])
q.parse_input()
q.print_output()
        