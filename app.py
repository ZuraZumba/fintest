#!/usr/bin/python3

# WRONG 4 jvymlbigecpfduqtozahknwxrs

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
        m = yy % 100
        l = yy // 100
        b = (dd + ((13 * mm) // 5) + m + (m // 4) + (l // 4) - 2 * l + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][b])
from sys import argv

i = DayOfWeekCalculator(argv[1])
i.parse_input()
i.print_output()
        