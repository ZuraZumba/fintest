#!/usr/bin/python3

# WRONG 6 evthajurdwikmfbxczpqsoygln

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        s = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(s.group(1), 10)
        self.m = int(s.group(2), 10)
        self.d = int(s.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        h = yy % 100
        a = yy // 100
        j = (dd + ((13 * mm) // 5) + h + (h // 4) + (a // 4) - 2 * a + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][j])
from sys import argv

u = DayOfWeekCalculator(argv[1])
u.parse_input()
u.print_output()
        