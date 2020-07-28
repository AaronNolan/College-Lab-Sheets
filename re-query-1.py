#!/usr/bin/env python

import sys

t = sys.argv[1].split("=")
field = t[0]
value = t[1]

l = sys.stdin.readlines()
s = l[0].split(",")

j = 0
while j < len(s):
    if s[j].strip() == field:
        n = j
    j += 1

i = 1
while i < len(l):
    a = l[i].split(",")
    if a[n] == value:
        print(l[i].strip())
    i += 1
