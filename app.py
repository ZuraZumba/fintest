#!/usr/bin/python3

# RIGHT 4 abyxscmegzuqowdvirnptlhjkf

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        t = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(t.group(1), 10)
        self.m = int(t.group(2), 10)
        self.d = int(t.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        x = yy % 100
        s = yy // 100
        c = (dd + ((13 * mm) // 5) + x + (x // 4) + (s // 4) - 2 * s + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][c])
from sys import argv

m = DayOfWeekCalculator(argv[1])
m.parse_input()
m.print_output()
        