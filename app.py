#!/usr/bin/python3

# RIGHT 3 iuwdnqvjkxalrescgzpytomfbh

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
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        d = yy % 100
        n = yy // 100
        q = (dd + ((13 * (mm + 1)) // 5) + d + (d // 4) + (n // 4) - 2 * n + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

v = DayOfWeekCalculator(argv[1])
v.parse_input()
v.print_output()
        