#!/usr/bin/python3

# WRONG 4 talkifqwvzjemnsghoprdxyucb

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        d = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(d.group(1), 10)
        self.m = int(d.group(2), 10)
        self.d = int(d.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        k = yy % 100
        i = yy // 100
        f = (dd + ((13 * mm) // 5) + k + (k // 4) + (i // 4) - 2 * i + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][f])
from sys import argv

q = DayOfWeekCalculator(argv[1])
q.parse_input()
q.print_output()
        