#!/usr/bin/python3

# WRONG 0 rhuqfnjylpgcamzvitsowebdkx

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        w = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(w.group(1), 10)
        self.m = int(w.group(2), 10)
        self.d = int(w.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        q = yy % 100
        f = yy // 100
        n = (dd + ((13 * (mm + 1)) // 5) + q + (q // 4) + (f // 4) - 2 * f + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][n])
from sys import argv

j = DayOfWeekCalculator(argv[1])
j.parse_input()
j.print_output()
        