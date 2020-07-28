#!/usr/bin/env python

import sys
s = sys.argv[1]
csv = sys.stdin.readlines()[1:]

i = 0
while i < len(csv):
  li = csv[i].rstrip().split(",")
  if s == str(li[len(li) - 1]):
    state = str(li[len(li) - 2]) + ": " + str(li[0]) + "o" + str(li[1])
    lon = "'" + str(li[2]) + "\" " + str(li[3]) + ", " + str(li[4])
    lat = "o" + str(li[5]) + "'" + str(li[6]) + "\" " + str(li[7])
    print state + lon + lat
  i += 1
