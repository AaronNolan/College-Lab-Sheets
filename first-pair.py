#!/usr/bin/env python

import sys

s = sys.stdin.readline()
i = 0
while i < len(s):
    if i != len(s) - 1:
        if s[i] == s[i + 1]:
            print(s[i:i + 2])
            i = len(s)
    i += 1
