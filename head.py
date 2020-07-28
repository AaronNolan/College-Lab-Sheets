#!/usr/bin/env python

import sys
n = sys.argv[1]
l = sys.stdin.readlines()
i = 0
if len(l) > int(n):
    while i < int(n):
        print(l[i].strip())
        i += 1
else:
    while i < len(l):
        print(l[i].strip())
        i += 1
