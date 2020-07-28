#!/usr/bin/env python

import sys

s = sys.stdin.readline()
a = ""
n = ""
i = 0
while i < len(s):
    if "A" <= s[i] and s[i] <= "Z":
        a += s[i]
        n = str(i)
        if i < len(s) - 1:
            if "A" > s[i + 1] and not s[i + 1] > "Z":
                i = len(s) - 1
    i += 1

if n != "":
    n = str(int(n) - len(a) + 1)
    print(str(a) + " " + str(n))
