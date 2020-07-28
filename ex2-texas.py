#!/usr/bin/env python

import sys

li = sys.stdin.readlines()

i = 1
while i < len(li):
  s = li[i].rstrip().split(",")
  if s[9] == "TX":
    print s[8]
  i += 1
