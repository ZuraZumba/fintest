#!/usr/bin/python3

# RIGHT 3 hbrfyelumxsqpowzjgvincdtak

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
        if self.m >= 3:
            mm = self.m
            yy = self.y
        else:
            mm = self.m + 12
            yy = self.y - 1
        f = yy % 100
        y = yy // 100
        e = (dd + ((13 * (mm + 1)) // 5) + f + (f // 4) + (y // 4) - 2 * y + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][e])
from sys import argv

l = DayOfWeekCalculator(argv[1])
l.parse_input()
l.print_output()
        