#!/usr/bin/python3

# RIGHT 3 kcwfdhpetziumyvqglnbaorxjs

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        a = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(a.group(1), 10)
        self.m = int(a.group(2), 10)
        self.d = int(a.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        f = yy % 100
        d = yy // 100
        h = (dd + ((13 * (mm + 1)) // 5) + f + (f // 4) + (d // 4) - 2 * d + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][h])
from sys import argv

p = DayOfWeekCalculator(argv[1])
p.parse_input()
p.print_output()
        