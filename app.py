#!/usr/bin/python3

# WRONG 2 iupcwvdfyhjmqgslzarekbotnx

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
        if self.m > 2:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        c = yy % 100
        w = yy // 100
        v = (dd + ((13 * (mm + 1)) // 5) + c + (c // 4) + (w // 4) - 2 * w + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][v])
from sys import argv

d = DayOfWeekCalculator(argv[1])
d.parse_input()
d.print_output()
        