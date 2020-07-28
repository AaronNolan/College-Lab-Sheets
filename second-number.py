#!/usr/bin/env python

import sys

s = sys.stdin.readline()
i = 0
n = ""  # Create a variable to add each number found
l = []  # A list with all the numbers n
m = []  # Where it is in the string
while i < len(s):
    if "0" <= s[i] <= "9":  # Check if character is a number
        n = n + str(s[i])
        if i + 1 < len(s):
            if not ("0" <= s[i + 1] <= "9"):
                l.append(n)
                m.append(i - len(n) + 1)
                n = ""
    i = i + 1

if len(l) > 1:
    print(l[1] + " " + str(m[1]))
