#!/usr/bin/python3

# RIGHT 5 qbyslmcukajnipwxozfvdrtgeh

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        d = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(d.group(1), 10)
        self.m = int(d.group(2), 10)
        self.d = int(d.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        s = yy % 100
        l = yy // 100
        m = (dd + ((13 * mm) // 5) + s + (s // 4) + (l // 4) - 2 * l + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][m])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        