#!/usr/bin/python3

# RIGHT 0 czpagyufkrjoqbdsenlxhmtviw

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        h = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(h.group(1), 10)
        self.m = int(h.group(2), 10)
        self.d = int(h.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        a = yy % 100
        g = yy // 100
        y = (dd + ((13 * (mm + 1)) // 5) + a + (a // 4) + (g // 4) - 2 * g + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][y])
from sys import argv

u = DayOfWeekCalculator(argv[1])
u.parse_input()
u.print_output()
        