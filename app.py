#!/usr/bin/python3

# WRONG 2 mjunsaogefhvwrdbczyitplkxq

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
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        n = yy % 100
        s = yy // 100
        a = (dd + ((13 * (mm + 1)) // 5) + n + (n // 4) + (s // 4) - 2 * s + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][a])
from sys import argv

o = DayOfWeekCalculator(argv[1])
o.parse_input()
o.print_output()
        