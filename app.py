#!/usr/bin/python3

# WRONG 6 xpuzkcgetvlyomhfdaiqbnrjsw

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
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        z = yy % 100
        k = yy // 100
        c = (dd + ((13 * mm) // 5) + z + (z // 4) + (k // 4) - 2 * k + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][c])
from sys import argv

g = DayOfWeekCalculator(argv[1])
g.parse_input()
g.print_output()
        