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
  if str(s[0]) == str(li[len(li) - 2]):
    if str(s[1]) == str(li[len(li) - 1]):
      lat = seconds(int(li[0]), int(li[1]), int(li[2]))
      lon = seconds(int(li[4]), int(li[5]), int(li[6]))
      print str(lat) + " " + str(lon)
  i += 1
