#!/usr/bin/python3

# WRONG 3 yltsnmjiqbzpcuhegfadvrowxk

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        v = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(v.group(1), 10)
        self.m = int(v.group(2), 10)
        self.d = int(v.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        s = yy % 100
        n = yy // 100
        m = (dd + ((13 * (mm + 1)) // 5) + s + (s // 4) + (n // 4) - 2 * n + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][m])
from sys import argv

j = DayOfWeekCalculator(argv[1])
j.parse_input()
j.print_output()
        