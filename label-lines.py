#!/usr/bin/env python

s = raw_input()
li = []
while s != "end":
    li.append(s)
    s = raw_input()
i = 0
while i < len(li):
    print str(i) + " " + str(len(li)) + " " + str(li[i])
    i += 1
