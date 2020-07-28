#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
  li = f.readlines()

numbers = []
i = 0
while i < len(li):
  l = li[i].strip().split(" ")
  j = 0
  while j < len(l):
    numbers.append(l[j])
    j += 1
  i += 1

i = 0
t = 0
while i < len(numbers):
  if len(str(numbers[i])) != 0:
    t = t + int(numbers[i])
  i += 1
print t
