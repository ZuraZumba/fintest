#!/usr/bin/python3

# WRONG 0 myhsoizwbncaduqfjveklrgxpt

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
        s = yy % 100
        o = yy // 100
        i = (dd + ((13 * (mm + 1)) // 5) + s + (s // 4) + (o // 4) - 2 * o + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i])
from sys import argv

z = DayOfWeekCalculator(argv[1])
z.parse_input()
z.print_output()
        