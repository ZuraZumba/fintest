#!/usr/bin/python3

# RIGHT 7 vdkrfxpqbuojcngswhltmezaiy

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        m = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(m.group(1), 10)
        self.m = int(m.group(2), 10)
        self.d = int(m.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        r = yy % 100
        f = yy // 100
        x = (dd + ((13 * mm) // 5) + r + (r // 4) + (f // 4) - 2 * f + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])
from sys import argv

p = DayOfWeekCalculator(argv[1])
p.parse_input()
p.print_output()
        