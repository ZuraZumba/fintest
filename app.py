#!/usr/bin/python3

# WRONG 4 yskzvoeharqbtdpifcwxjungml

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        j = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(j.group(1), 10)
        self.m = int(j.group(2), 10)
        self.d = int(j.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        z = yy % 100
        v = yy // 100
        o = (dd + ((13 * mm) // 5) + z + (z // 4) + (v // 4) - 2 * v + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][o])
from sys import argv

e = DayOfWeekCalculator(argv[1])
e.parse_input()
e.print_output()
        