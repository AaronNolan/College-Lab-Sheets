#!/usr/bin/env python

import sys
t = sys.argv[1]
l = sys.stdin.readlines()
s = l[0].split(",")

j = 0
while j < len(s):
    if s[j].strip() == t:
        n = j
    j += 1

i = 1
while i < len(l):
    t = l[i].split(",")
    print(t[n].strip())
    i += 1
