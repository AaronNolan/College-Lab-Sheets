#!/usr/bin/env python

import sys
s = sys.argv[1:]
csv = sys.stdin.readlines()[1:]


def seconds(d, m, s):
  d = d * 60 * 60
  m = m * 60
  a = d + m + s
  return a


i = 0
while i < len(csv):
  li = csv[i].rstrip().split(",")
  lon = seconds(int(li[4]), int(li[5]), int(li[6]))
  if int(s[0]) < int(lon) < int(s[1]):
    print str(li[len(li) - 2]) + ", " + str(li[len(li) - 1])
  i += 1
