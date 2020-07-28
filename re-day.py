#!/usr/bin/env python

import sys
day = sys.argv[1]
l = sys.stdin.readlines()
i = 1
while i < len(l):
    s = l[i].split(",")
    t = s[8]
    if t[0:3] == str(day):
        print(l[i].strip())
    i += 1
