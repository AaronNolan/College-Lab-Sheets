#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
    if "A" <= s[i] <= "Z":
        print s[i]
    i += 1
