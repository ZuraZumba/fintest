#!/usr/bin/python3

# WRONG 7 owzbxcplysjgvfqmhkueiadtrn

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        i = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(i.group(1), 10)
        self.m = int(i.group(2), 10)
        self.d = int(i.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        b = yy % 100
        x = yy // 100
        c = (dd + ((13 * mm) // 5) + b + (b // 4) + (x // 4) - 2 * x + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][c])
from sys import argv

p = DayOfWeekCalculator(argv[1])
p.parse_input()
p.print_output()
        