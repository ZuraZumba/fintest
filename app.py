#!/usr/bin/python3

# RIGHT 6 srhvamcpxgduobfeyitkqjlzwn

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
        if self.m > 2:
            mm = self.m + 1
            yy = self.y
        else:
            mm = self.m + 13
            yy = self.y - 1
        v = yy % 100
        a = yy // 100
        m = (dd + ((13 * mm) // 5) + v + (v // 4) + (a // 4) - 2 * a + 5) % 7
        print(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][m])
from sys import argv

c = DayOfWeekCalculator(argv[1])
c.parse_input()
c.print_output()
        