#!/usr/bin/python3

# WRONG 6 aptxmhjswrkeqogydbzuivfcln

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        i = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(i.group(1), 10)
        self.m = int(i.group(2), 10)
        self.d = int(i.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        x = yy % 100
        m = yy // 100
        h = (dd + ((13 * mm) // 5) + x + (x // 4) + (m // 4) - 2 * m + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][h])
from sys import argv

j = DayOfWeekCalculator(argv[1])
j.parse_input()
j.print_output()
        