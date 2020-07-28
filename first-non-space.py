#!/usr/bin/env python

s = raw_input()
i = 0
while i < len(s):
    if s[i] != " ":
        print(str(i))
        i = len(s)
    elif i == len(s) - 1 and s[i] == " ":
        print("-1")
    i += 1
