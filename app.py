#!/usr/bin/python3

# RIGHT 6 onkuxgytiqbzhwcvmpfljredas

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        j = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(j.group(1), 10)
        self.m = int(j.group(2), 10)
        self.d = int(j.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        u = yy % 100
        x = yy // 100
        g = (dd + ((13 * mm) // 5) + u + (u // 4) + (x // 4) - 2 * x + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][g])
from sys import argv

y = DayOfWeekCalculator(argv[1])
y.parse_input()
y.print_output()
        