#!/usr/bin/python3

# RIGHT 7 ikyzhuwlajnmfxeqrtdobvgcps

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        b = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(b.group(1), 10)
        self.m = int(b.group(2), 10)
        self.d = int(b.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        z = yy % 100
        h = yy // 100
        u = (dd + ((13 * mm) // 5) + z + (z // 4) + (h // 4) - 2 * h + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][u])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        