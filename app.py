#!/usr/bin/python3

# WRONG 5 yadmcutxgiqlzsvwfenkjrhpbo

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        j = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(j.group(1), 10)
        self.m = int(j.group(2), 10)
        self.d = int(j.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        m = yy % 100
        c = yy // 100
        u = (dd + ((13 * mm) // 5) + m + (m // 4) + (c // 4) - 2 * c + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

t = DayOfWeekCalculator(argv[1])
t.parse_input()
t.print_output()
        