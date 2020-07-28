#!/usr/bin/env python

import sys
s = str(sys.argv[1])
csv = sys.stdin.readlines()[1:]

i = 0
while i < len(csv):
  li = csv[i].rstrip().split(",")
  if s == str(li[len(li) - 1]):
    print str(li[len(li) - 2])
  i += 1
