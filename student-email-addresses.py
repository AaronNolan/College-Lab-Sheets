#!/usr/bin/env python

s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()

i = 0
while i < len(l):
    s = l[i].split(",")
    print("".join(s[1]))
    i += 1
