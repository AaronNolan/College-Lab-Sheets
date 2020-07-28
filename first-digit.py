#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
    if "0" <= s[i] and s[i] <= "9":
        print("".join(s[i]) + " " + str(i))
        i = len(s)
    i += 1
