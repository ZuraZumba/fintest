#!/usr/bin/python3

# RIGHT 7 kghimnfpxsrzvtdawblyqojeuc

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
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        i = yy % 100
        m = yy // 100
        n = (dd + ((13 * mm) // 5) + i + (i // 4) + (m // 4) - 2 * m + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][n])
from sys import argv

f = DayOfWeekCalculator(argv[1])
f.parse_input()
f.print_output()
        