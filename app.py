#!/usr/bin/python3

# WRONG 7 muodjhelniqtckfypwvxaszrbg

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        a = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(a.group(1), 10)
        self.m = int(a.group(2), 10)
        self.d = int(a.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        d = yy % 100
        j = yy // 100
        h = (dd + ((13 * mm) // 5) + d + (d // 4) + (j // 4) - 2 * j + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][h])
from sys import argv

e = DayOfWeekCalculator(argv[1])
e.parse_input()
e.print_output()
        