#!/usr/bin/python3

# RIGHT 3 idepgkohcvyxqjtfnlamzubwrs

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        z = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(z.group(1), 10)
        self.m = int(z.group(2), 10)
        self.d = int(z.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        p = yy % 100
        g = yy // 100
        k = (dd + ((13 * (mm + 1)) // 5) + p + (p // 4) + (g // 4) - 2 * g + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][k])
from sys import argv

o = DayOfWeekCalculator(argv[1])
o.parse_input()
o.print_output()
        