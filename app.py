#!/usr/bin/python3

# RIGHT 6 kobrwnqzxejutglcsypaifhdvm

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        i = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(i.group(1), 10)
        self.m = int(i.group(2), 10)
        self.d = int(i.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        r = yy % 100
        w = yy // 100
        n = (dd + ((13 * mm) // 5) + r + (r // 4) + (w // 4) - 2 * w + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][n])
from sys import argv

q = DayOfWeekCalculator(argv[1])
q.parse_input()
q.print_output()
        