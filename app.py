#!/usr/bin/python3

# WRONG 7 cwdinumrshgljtfzvbqxkyoepa

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        k = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(k.group(1), 10)
        self.m = int(k.group(2), 10)
        self.d = int(k.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        i = yy % 100
        n = yy // 100
        u = (dd + ((13 * mm) // 5) + i + (i // 4) + (n // 4) - 2 * n + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

m = DayOfWeekCalculator(argv[1])
m.parse_input()
m.print_output()
        