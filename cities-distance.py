#!/usr/bin/env python

import sys
import math
s = sys.argv[1:]
csv = sys.stdin.readlines()[1:]


def seconds(d, m, s):
  d = d * 60 * 60
  m = m * 60
  a = d + m + s
  return a


def state_lat_lon(csv, s):
  i = 0
  while i < len(csv):
    li = csv[i].rstrip().split(",")
    if str(s[0]) == str(li[len(li) - 2]):
      if str(s[1]) == str(li[len(li) - 1]):
        lat = seconds(int(li[0]), int(li[1]), int(li[2]))
        lon = seconds(int(li[4]), int(li[5]), int(li[6]))
    i += 1
  return str(lat) + " " + str(lon)

x1_y1 = state_lat_lon(csv, s).split(" ")
x2_y2 = state_lat_lon(csv, s[2:]).split(" ")

x1 = int(x1_y1[0])
x2 = int(x2_y2[0])
y1 = int(x1_y1[1])
y2 = int(x2_y2[1])

x = (x2 - x1) ** 2
y = (y2 - y1) ** 2

d = math.sqrt(x + y)
a = ((d / 60) / 60) * 111

if a % 1 > .5:
  print int(a) + 1
else:
  print int(a)
