#!/usr/bin/python3

# WRONG 6 lfzcsvoneubthgyxjrkiaqwdmp

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        a = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(a.group(1), 10)
        self.m = int(a.group(2), 10)
        self.d = int(a.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        c = yy % 100
        s = yy // 100
        v = (dd + ((13 * mm) // 5) + c + (c // 4) + (s // 4) - 2 * s + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

o = DayOfWeekCalculator(argv[1])
o.parse_input()
o.print_output()
        