#!/usr/bin/python3

# WRONG 7 wlbtrcfhgoeadysmqkipujnvxz

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        u = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(u.group(1), 10)
        self.m = int(u.group(2), 10)
        self.d = int(u.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        t = yy % 100
        r = yy // 100
        c = (dd + ((13 * mm) // 5) + t + (t // 4) + (r // 4) - 2 * r + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][c])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        