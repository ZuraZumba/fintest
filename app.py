#!/usr/bin/python3

# WRONG 4 osbhpiqmfxktwgjeavncydrulz

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
        h = yy % 100
        p = yy // 100
        i = (dd + ((13 * mm) // 5) + h + (h // 4) + (p // 4) - 2 * p + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][i])
from sys import argv

q = DayOfWeekCalculator(argv[1])
q.parse_input()
q.print_output()
        