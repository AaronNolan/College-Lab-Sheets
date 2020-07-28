#!/usr/bin/env python

s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()

i = 0
while i < len(l):
    s = l[i].split(",")
    if len(s[5]) > 2:
        print("".join(s[0] + " " + "".join(s[5])))
    i += 1
