#!/usr/bin/python3

# RIGHT 3 iakdotxwzsnyfbvrcmuqejhlpg

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
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        d = yy % 100
        o = yy // 100
        t = (dd + ((13 * (mm + 1)) // 5) + d + (d // 4) + (o // 4) - 2 * o + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][t])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        