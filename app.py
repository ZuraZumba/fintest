#!/usr/bin/python3

# RIGHT 1 ritosfwdbqzpgvnjumkexchaly

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        x = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(x.group(1), 10)
        self.m = int(x.group(2), 10)
        self.d = int(x.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        o = yy % 100
        s = yy // 100
        f = (dd + ((13 * (mm + 1)) // 5) + o + (o // 4) + (s // 4) - 2 * s + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][f])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        