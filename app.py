#!/usr/bin/python3

# RIGHT 5 gjonmytzpxvesrdcfqbuliawkh

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        l = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(l.group(1), 10)
        self.m = int(l.group(2), 10)
        self.d = int(l.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        n = yy % 100
        m = yy // 100
        y = (dd + ((13 * mm) // 5) + n + (n // 4) + (m // 4) - 2 * m + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][y])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        