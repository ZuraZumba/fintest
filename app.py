#!/usr/bin/python3

# WRONG 6 zhkboagcpjxiwsymqurtefnvdl

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
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        b = yy % 100
        o = yy // 100
        a = (dd + ((13 * mm) // 5) + b + (b // 4) + (o // 4) - 2 * o + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][a])
from sys import argv

g = DayOfWeekCalculator(argv[1])
g.parse_input()
g.print_output()
        