#!/usr/bin/python3

# WRONG 7 cflaqxkrtbhenowpzmigyudvjs

class DayOfWeekCalculator:
    def __init__(self, input:str):
        self.i = input
        self.y = None
        self.m = None
        self.d = None

    def parse_input(self):
        from re import fullmatch

        y = fullmatch("(\d{4})-(\d{2})-(\d{2})", self.i)

        self.y = int(y.group(1), 10)
        self.m = int(y.group(2), 10)
        self.d = int(y.group(3), 10)

    def print_output(self):
        dd = self.d
        if self.m >= 3:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        a = yy % 100
        q = yy // 100
        x = (dd + ((13 * mm) // 5) + a + (a // 4) + (q // 4) - 2 * q + 8) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])
from sys import argv

k = DayOfWeekCalculator(argv[1])
k.parse_input()
k.print_output()
        