#!/usr/bin/env python

import sys
name = sys.argv[1]
l = sys.stdin.readlines()
i = 0
while i < len(l):
    s = l[i].split(",")
    if s[1] == str(name):
        print(l[i].strip())
    i += 1
