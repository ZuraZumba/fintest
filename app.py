#!/usr/bin/python3

# WRONG 3 plnjatbcuqfgyhewrsivxmozdk

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        x = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(x.group(1), 10)
        self.m = int(x.group(2), 10)
        self.d = int(x.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        j = yy % 100
        a = yy // 100
        t = (dd + ((13 * (mm + 1)) // 5) + j + (j // 4) + (a // 4) - 2 * a + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][t])
from sys import argv

b = DayOfWeekCalculator(argv[1])
b.parse_input()
b.print_output()
        