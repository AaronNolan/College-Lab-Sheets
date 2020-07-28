#!/usr/bin/env python

import sys
n = sys.argv[1]
l = sys.stdin.readlines()
i = int(n)
if len(l) > int(n):
    while i > 0:
        print(l[len(l) - i].strip())
        i -= 1
else:
    i = 0
    while i < len(l):
        print(l[i].strip())
        i += 1
