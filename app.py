#!/usr/bin/python3

# WRONG 6 tcolezjywnbfvrsdiuaqgxmkhp

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        g = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(g.group(1), 10)
        self.m = int(g.group(2), 10)
        self.d = int(g.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        l = yy % 100
        e = yy // 100
        z = (dd + ((13 * mm) // 5) + l + (l // 4) + (e // 4) - 2 * e + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][z])
from sys import argv

j = DayOfWeekCalculator(argv[1])
j.parse_input()
j.print_output()
        