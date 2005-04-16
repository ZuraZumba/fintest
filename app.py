#!/usr/bin/python3

# WRONG 4 xhopumejidwzvtrbqgyaklsfnc

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        k = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(k.group(1), 10)
        self.m = int(k.group(2), 10)
        self.d = int(k.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        p = yy % 100
        u = yy // 100
        m = (dd + ((13 * mm) // 5) + p + (p // 4) + (u // 4) - 2 * u + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][m])
from sys import argv

e = DayOfWeekCalculator(argv[1])
e.parse_input()
e.print_output()
        