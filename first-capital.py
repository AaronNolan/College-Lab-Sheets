#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
    if "A" <= s[i] and s[i] <= "Z":
        print("".join(s[i]) + " " + str(i))
        i = len(s)
    i += 1
