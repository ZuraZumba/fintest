#!/usr/bin/python3

# RIGHT 7 aujnykosprqwghediflxbzvcmt

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        b = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(b.group(1), 10)
        self.m = int(b.group(2), 10)
        self.d = int(b.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        n = yy % 100
        y = yy // 100
        k = (dd + ((13 * mm) // 5) + n + (n // 4) + (y // 4) - 2 * y + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][k])
from sys import argv

o = DayOfWeekCalculator(argv[1])
o.parse_input()
o.print_output()
        