#!/usr/bin/python3

# WRONG 0 gbdiwsapekrnxvqmtozcluhyfj

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        l = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(l.group(1), 10)
        self.m = int(l.group(2), 10)
        self.d = int(l.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        i = yy % 100
        w = yy // 100
        s = (dd + ((13 * (mm + 1)) // 5) + i + (i // 4) + (w // 4) - 2 * w + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][s])
from sys import argv

a = DayOfWeekCalculator(argv[1])
a.parse_input()
a.print_output()
        