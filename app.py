#!/usr/bin/python3

# WRONG 4 axdypsbrjltmnuoqweifckvzgh

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
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        y = yy % 100
        p = yy // 100
        s = (dd + ((13 * mm) // 5) + y + (y // 4) + (p // 4) - 2 * p + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][s])
from sys import argv

b = DayOfWeekCalculator(argv[1])
b.parse_input()
b.print_output()
        