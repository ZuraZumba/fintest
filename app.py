#!/usr/bin/python3

# WRONG 5 znfapuwqrmblyegkxsjticohvd

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
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        a = yy % 100
        p = yy // 100
        u = (dd + ((13 * mm) // 5) + a + (a // 4) + (p // 4) - 2 * p + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        