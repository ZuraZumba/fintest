#!/usr/bin/python3

# WRONG 5 iecjayhbusgqktxmvprlfnwzdo

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        f = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(f.group(1), 10)
        self.m = int(f.group(2), 10)
        self.d = int(f.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m >= 3 else self.m + 13
        yy = self.y if self.m >= 3 else self.y - 1
        j = yy % 100
        a = yy // 100
        y = (dd + ((13 * mm) // 5) + j + (j // 4) + (a // 4) - 2 * a + 7) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][y])
from sys import argv

h = DayOfWeekCalculator(argv[1])
h.parse_input()
h.print_output()
        