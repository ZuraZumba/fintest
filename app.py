#!/usr/bin/python3

# WRONG 4 fduszcxablvpjwnemitoykhrqg

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        y = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(y.group(1), 10)
        self.m = int(y.group(2), 10)
        self.d = int(y.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        s = yy % 100
        z = yy // 100
        c = (dd + ((13 * mm) // 5) + s + (s // 4) + (z // 4) - 2 * z + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][c])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        