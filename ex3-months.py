#!/usr/bin/env python

import sys

li = sys.stdin.readlines()
dates = []
i = 0
while i < len(li):
  l = li[i].split()
  j = 0
  while j < len(l):
    dates.append(l[j])
    j += 1
  i += 1

i = 0
while i < len(dates):
  print dates[i].split("/")[1]
  i += 1
