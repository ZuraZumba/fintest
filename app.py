#!/usr/bin/python3

# RIGHT 2 mpiceqkybzgsnltourvwadfjhx

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        a = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(a.group(1), 10)
        self.m = int(a.group(2), 10)
        self.d = int(a.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        c = yy % 100
        e = yy // 100
        q = (dd + ((13 * (mm + 1)) // 5) + c + (c // 4) + (e // 4) - 2 * e + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

k = DayOfWeekCalculator(argv[1])
k.parse_input()
k.print_output()
        