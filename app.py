#!/usr/bin/python3

# RIGHT 1 sanxkzvoyfjqldhcbgewtrpumi

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        t = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(t.group(1), 10)
        self.m = int(t.group(2), 10)
        self.d = int(t.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        x = yy % 100
        k = yy // 100
        z = (dd + ((13 * (mm + 1)) // 5) + x + (x // 4) + (k // 4) - 2 * k + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][z])
from sys import argv

v = DayOfWeekCalculator(argv[1])
v.parse_input()
v.print_output()
        