#!/usr/bin/env python

import sys
li = sys.stdin.readlines()
counts = {}
i = 0
while i < len(li):
  list_m = li[i].strip().split("/")
  s = int(list_m[1])
  if s not in counts:
    counts[s] = 0
  counts[s] = counts[s] + 1
  i += 1

for s in counts:
  print s, counts[s]
