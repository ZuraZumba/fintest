#!/usr/bin/python3

# WRONG 2 ersmnjlhtpoxfiaubqcgkwvdyz

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        k = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(k.group(1), 10)
        self.m = int(k.group(2), 10)
        self.d = int(k.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        m = yy % 100
        n = yy // 100
        j = (dd + ((13 * (mm + 1)) // 5) + m + (m // 4) + (n // 4) - 2 * n + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

l = DayOfWeekCalculator(argv[1])
l.parse_input()
l.print_output()
        