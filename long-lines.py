#!/usr/bin/env python

s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()
n = input()
i = 0
while i < len(l):
    if len(l[i]) > n:
        print str(l[i])
    i += 1
