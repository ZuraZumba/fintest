#!/usr/bin/python3

# WRONG 6 ldxzhugfsaotvpiybjmqnkrecw

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        n = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(n.group(1), 10)
        self.m = int(n.group(2), 10)
        self.d = int(n.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        z = yy % 100
        h = yy // 100
        u = (dd + ((13 * mm) // 5) + z + (z // 4) + (h // 4) - 2 * h + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

g = DayOfWeekCalculator(argv[1])
g.parse_input()
g.print_output()
        