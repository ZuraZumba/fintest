#!/usr/bin/python3

# WRONG 7 vxlqrinazpjoectugwdksymfhb

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        s = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(s.group(1), 10)
        self.m = int(s.group(2), 10)
        self.d = int(s.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        q = yy % 100
        r = yy // 100
        i = (dd + ((13 * mm) // 5) + q + (q // 4) + (r // 4) - 2 * r + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i])
from sys import argv

n = DayOfWeekCalculator(argv[1])
n.parse_input()
n.print_output()
        