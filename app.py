#!/usr/bin/python3

# WRONG 7 lqrhbgcvmextnkuswdojfaipzy

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        f = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(f.group(1), 10)
        self.m = int(f.group(2), 10)
        self.d = int(f.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        h = yy % 100
        b = yy // 100
        g = (dd + ((13 * mm) // 5) + h + (h // 4) + (b // 4) - 2 * b + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][g])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        