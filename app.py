#!/usr/bin/python3

# WRONG 6 txedlniapwqrkmvujfbsyoczgh

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
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        d = yy % 100
        l = yy // 100
        n = (dd + ((13 * mm) // 5) + d + (d // 4) + (l // 4) - 2 * l + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][n])
from sys import argv

i = DayOfWeekCalculator(argv[1])
i.parse_input()
i.print_output()
        