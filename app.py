#!/usr/bin/python3

# RIGHT 4 vzwfbjysuikmonthrxlecagqpd

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
        f = yy % 100
        b = yy // 100
        j = (dd + ((13 * mm) // 5) + f + (f // 4) + (b // 4) - 2 * b + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

y = DayOfWeekCalculator(argv[1])
y.parse_input()
y.print_output()
        