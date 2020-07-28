#!/usr/bin/env python

import sys
t = sys.argv[1]
s = sys.stdin.readline().split(",")
j = 0
while j < len(s):
    if s[j].strip() == t:
        print(j)
    j += 1
