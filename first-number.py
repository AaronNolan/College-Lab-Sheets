#!/usr/bin/env python

import sys

s = sys.stdin.readline()
a = ""
n = ""
i = 0
while i < len(s):
    if "1" <= s[i] and s[i] <= "9":
        a += s[i]
        n = str(i)
        if i < len(s) - 1:
            if "1" > s[i + 1] and not s[i + 1] > "9":
                i = len(s) - 1
    i += 1

if n != "":
    n = str(int(n) - len(a) + 1)
    print(str(a) + " " + str(n))
