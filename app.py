#!/usr/bin/python3

# WRONG 7 srxuyjwbzhnlogmvfiqdectkap

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        e = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(e.group(1), 10)
        self.m = int(e.group(2), 10)
        self.d = int(e.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        u = yy % 100
        y = yy // 100
        j = (dd + ((13 * mm) // 5) + u + (u // 4) + (y // 4) - 2 * y + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        