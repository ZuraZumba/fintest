#!/usr/bin/python3

# WRONG 3 gnsxldctkeqbhvjpyfmiuawzor

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        u = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(u.group(1), 10)
        self.m = int(u.group(2), 10)
        self.d = int(u.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        x = yy % 100
        l = yy // 100
        d = (dd + ((13 * (mm + 1)) // 5) + x + (x // 4) + (l // 4) - 2 * l + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][d])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        