#!/usr/bin/python3

# RIGHT 7 rhzcapxqmkfitlgsuvnbjyeowd

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        j = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(j.group(1), 10)
        self.m = int(j.group(2), 10)
        self.d = int(j.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        c = yy % 100
        a = yy // 100
        p = (dd + ((13 * mm) // 5) + c + (c // 4) + (a // 4) - 2 * a + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][p])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        