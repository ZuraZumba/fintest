#!/usr/bin/python3

# WRONG 6 quhjrlnkwixcygsdzbemptofva

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
        j = yy % 100
        r = yy // 100
        l = (dd + ((13 * mm) // 5) + j + (j // 4) + (r // 4) - 2 * r + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][l])
from sys import argv

n = DayOfWeekCalculator(argv[1])
n.parse_input()
n.print_output()
        