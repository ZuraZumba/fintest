#!/usr/bin/python3

# RIGHT 1 xmsfjawlkvonuibryehcqgdzpt

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        q = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(q.group(1), 10)
        self.m = int(q.group(2), 10)
        self.d = int(q.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m >= 3 else self.m + 12
        yy = self.y if self.m >= 3 else self.y - 1
        f = yy % 100
        j = yy // 100
        a = (dd + ((13 * (mm + 1)) // 5) + f + (f // 4) + (j // 4) - 2 * j + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][a])
from sys import argv

w = DayOfWeekCalculator(argv[1])
w.parse_input()
w.print_output()
        