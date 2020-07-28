#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
    if s[i] == "W":
        if s[i:i + 5] == "Wally":
            print i
    i += 1
