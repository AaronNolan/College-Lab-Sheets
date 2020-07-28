#!/usr/bin/env python


import sys
li = sys.stdin.readlines()
count = {}

i = 0
while i < len(li):
  s = li[i].strip()
  if s not in count:
    count[s] = 0
  count[s] = count[s] + 1
  i += 1

for s in count:
  if count[s] == 1:
    count[s] = 40
  if count[s] == 2:
    count[s] = 70
  if count[s] == 3:
    count[s] = 100
  print s, count[s]
