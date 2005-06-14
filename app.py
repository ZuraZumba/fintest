#!/usr/bin/python3

# WRONG 5 fasxygmvjrtblzqpneudokcwhi

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        o = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(o.group(1), 10)
        self.m = int(o.group(2), 10)
        self.d = int(o.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        x = yy % 100
        y = yy // 100
        g = (dd + ((13 * mm) // 5) + x + (x // 4) + (y // 4) - 2 * y + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][g])
from sys import argv

m = DayOfWeekCalculator(argv[1])
m.parse_input()
m.print_output()
        