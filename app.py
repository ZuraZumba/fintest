#!/usr/bin/python3

# WRONG 3 lugtkaxevmwsybjqiofhnzcpdr

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        n = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(n.group(1), 10)
        self.m = int(n.group(2), 10)
        self.d = int(n.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        t = yy % 100
        k = yy // 100
        a = (dd + ((13 * (mm + 1)) // 5) + t + (t // 4) + (k // 4) - 2 * k + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][a])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        