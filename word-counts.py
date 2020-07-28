#!/usr/bin/env python

import sys

li = sys.stdin.readlines()
i = 0
while i < len(li):
    li_s = li[i].split()
    print(len(li_s))
    i += 1
