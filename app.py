#!/usr/bin/python3

# RIGHT 5 azqbrohyfnulvkwcdesjtgimpx

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
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        b = yy % 100
        r = yy // 100
        o = (dd + ((13 * mm) // 5) + b + (b // 4) + (r // 4) - 2 * r + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][o])
from sys import argv

h = DayOfWeekCalculator(argv[1])
h.parse_input()
h.print_output()
        