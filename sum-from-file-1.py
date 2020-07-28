#!/usr/bin/env python

with open("numbers.txt") as f:
  li = f.readlines()
i = 0
t = 0
while i < len(li):
  s = li[i].rstrip()
  t = t + int(s)
  i += 1
print t
