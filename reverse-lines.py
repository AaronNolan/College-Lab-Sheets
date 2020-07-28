#!/usr/bin/env python

s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()
i = 0
while i < len(l):
    print l[len(l) - i - 1]
    i += 1
