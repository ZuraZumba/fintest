#!/usr/bin/python3

# WRONG 6 eapgjxohmdcvblfyrqswuknizt

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        u = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(u.group(1), 10)
        self.m = int(u.group(2), 10)
        self.d = int(u.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        g = yy % 100
        j = yy // 100
        x = (dd + ((13 * mm) // 5) + g + (g // 4) + (j // 4) - 2 * j + 6) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])
from sys import argv

o = DayOfWeekCalculator(argv[1])
o.parse_input()
o.print_output()
        