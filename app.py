#!/usr/bin/python3

# WRONG 0 zxohvtiwqbpfdyaugmlrskjnce

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        s = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(s.group(1), 10)
        self.m = int(s.group(2), 10)
        self.d = int(s.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        h = yy % 100
        v = yy // 100
        t = (dd + ((13 * (mm + 1)) // 5) + h + (h // 4) + (v // 4) - 2 * v + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][t])
from sys import argv

i = DayOfWeekCalculator(argv[1])
i.parse_input()
i.print_output()
        