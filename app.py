#!/usr/bin/python3

# RIGHT 3 bphrcgjvdynuoiwltxzekqfams

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
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        r = yy % 100
        c = yy // 100
        g = (dd + ((13 * (mm + 1)) // 5) + r + (r // 4) + (c // 4) - 2 * c + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][g])
from sys import argv

j = DayOfWeekCalculator(argv[1])
j.parse_input()
j.print_output()
        