#!/usr/bin/python3

# WRONG 1 wrkyjuabelgzvisfoqxnmdthcp

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
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        y = yy % 100
        j = yy // 100
        u = (dd + ((13 * (mm + 1)) // 5) + y + (y // 4) + (j // 4) - 2 * j + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

a = DayOfWeekCalculator(argv[1])
a.parse_input()
a.print_output()
        