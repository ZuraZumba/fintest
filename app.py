#!/usr/bin/python3

# WRONG 2 rltpmgkqbhzdaijvcxuyfosewn

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        f = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(f.group(1), 10)
        self.m = int(f.group(2), 10)
        self.d = int(f.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        p = yy % 100
        m = yy // 100
        g = (dd + ((13 * (mm + 1)) // 5) + p + (p // 4) + (m // 4) - 2 * m + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][g])
from sys import argv

k = DayOfWeekCalculator(argv[1])
k.parse_input()
k.print_output()
        