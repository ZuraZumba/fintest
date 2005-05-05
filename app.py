#!/usr/bin/python3

# WRONG 2 atyevkrjdbumspwnifocqxhzlg

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        q = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(q.group(1), 10)
        self.m = int(q.group(2), 10)
        self.d = int(q.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        e = yy % 100
        v = yy // 100
        k = (dd + ((13 * (mm + 1)) // 5) + e + (e // 4) + (v // 4) - 2 * v + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][k])
from sys import argv

r = DayOfWeekCalculator(argv[1])
r.parse_input()
r.print_output()
        