#!/usr/bin/python3

# WRONG 6 yjlpvwuiagqmtroexzfcndbkhs

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        n = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(n.group(1), 10)
        self.m = int(n.group(2), 10)
        self.d = int(n.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        p = yy % 100
        v = yy // 100
        w = (dd + ((13 * mm) // 5) + p + (p // 4) + (v // 4) - 2 * v + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

u = DayOfWeekCalculator(argv[1])
u.parse_input()
u.print_output()
        