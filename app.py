#!/usr/bin/python3

# WRONG 4 blrtsqxnyfjvcdwzhamikegupo

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        k = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(k.group(1), 10)
        self.m = int(k.group(2), 10)
        self.d = int(k.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m + 1 if self.m > 2 else self.m + 13
        yy = self.y if self.m > 2 else self.y - 1
        t = yy % 100
        s = yy // 100
        q = (dd + ((13 * mm) // 5) + t + (t // 4) + (s // 4) - 2 * s + 11) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][q])
from sys import argv

x = DayOfWeekCalculator(argv[1])
x.parse_input()
x.print_output()
        