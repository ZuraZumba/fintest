#!/usr/bin/python3

# WRONG 0 dngmzwilyavtfqpsourchbxejk

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
        m = yy % 100
        z = yy // 100
        w = (dd + ((13 * (mm + 1)) // 5) + m + (m // 4) + (z // 4) - 2 * z + 9) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

i = DayOfWeekCalculator(argv[1])
i.parse_input()
i.print_output()
        