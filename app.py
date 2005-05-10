#!/usr/bin/python3

# WRONG 4 ayzrexjnbdkfompugwvltqihsc

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        t = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(t.group(1), 10)
        self.m = int(t.group(2), 10)
        self.d = int(t.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        r = yy % 100
        e = yy // 100
        x = (dd + ((13 * mm) // 5) + r + (r // 4) + (e // 4) - 2 * e + 10) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])
from sys import argv

j = DayOfWeekCalculator(argv[1])
j.parse_input()
j.print_output()
        