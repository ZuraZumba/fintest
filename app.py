#!/usr/bin/python3

# WRONG 5 uhlniravjkegxwzbqoctmypsdf

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        m = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(m.group(1), 10)
        self.m = int(m.group(2), 10)
        self.d = int(m.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        n = yy % 100
        i = yy // 100
        r = (dd + ((13 * mm) // 5) + n + (n // 4) + (i // 4) - 2 * i + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][r])
from sys import argv

a = DayOfWeekCalculator(argv[1])
a.parse_input()
a.print_output()
        