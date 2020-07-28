#!/usr/bin/env python

#Create a list of all the strings
s = raw_input()
l = []
while s != "end":
    l.append(s)
    s = raw_input()

#go through each string and print if true
i = 0
while i < len(l):
    s = l[i].split()
    if int(s[2]) > 1:
        print " ".join(s)
    i += 1
