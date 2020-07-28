#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
  li = f.readlines()
i = 0
t = 0
while i < len(li):
  s = li[i].rstrip()
  t = t + int(s)
  i += 1
print t
