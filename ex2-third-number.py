#!/usr/bin/env python

import sys

s = sys.stdin.readline()
positions = []
numbers = []
i = 0
while i < len(s):
  if "0" <= s[i] and s[i] <= "9":
    j = i + 1
    while j < len(s):
      if not("0" <= s[j] and s[j] <= "9"):
        numbers.append(s[i:j])
        positions.append(i)
        i = j
        j = len(s)
      j += 1
    if len(positions) == 3:
      print str(numbers[2]) + " " + str(positions[2])
  i += 1
