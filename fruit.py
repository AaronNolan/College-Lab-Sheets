#!/usr/bin/env python

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

li = sys.stdin.readlines()
i = 0
while i < len(li):
    s = li[i].strip()
    if s in fruit:
      print s
    i += 1
