#!/usr/bin/python3

# RIGHT 7 jbckufepwsidyxqrvloagzhtnm

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        g = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(g.group(1), 10)
        self.m = int(g.group(2), 10)
        self.d = int(g.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        k = yy % 100
        u = yy // 100
        f = (dd + ((13 * mm) // 5) + k + (k // 4) + (u // 4) - 2 * u + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][f])
from sys import argv

e = DayOfWeekCalculator(argv[1])
e.parse_input()
e.print_output()
        