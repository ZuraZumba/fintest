#!/usr/bin/python3

# RIGHT 0 byhlawdzsjfprxomqgtnciekvu

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        c = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(c.group(1), 10)
        self.m = int(c.group(2), 10)
        self.d = int(c.group(3), 10)

    def print_output(self):
        dd = self.d
        mm = self.m if self.m > 2 else self.m + 12
        yy = self.y if self.m > 2 else self.y - 1
        l = yy % 100
        a = yy // 100
        w = (dd + ((13 * (mm + 1)) // 5) + l + (l // 4) + (a // 4) - 2 * a + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][w])
from sys import argv

d = DayOfWeekCalculator(argv[1])
d.parse_input()
d.print_output()
        