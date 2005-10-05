#!/usr/bin/python3

# WRONG 6 asljubypfergqxdimnowchtkvz

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        c = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(c.group(1), 10)
        self.m = int(c.group(2), 10)
        self.d = int(c.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        j = yy % 100
        u = yy // 100
        b = (dd + ((13 * mm) // 5) + j + (j // 4) + (u // 4) - 2 * u + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][b])
from sys import argv

y = DayOfWeekCalculator(argv[1])
y.parse_input()
y.print_output()
        