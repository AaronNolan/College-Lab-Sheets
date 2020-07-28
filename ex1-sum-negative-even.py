#!/usr/bin/env python

s = raw_input()
t = 0
r = 0
while s != "end":
  if int(s) % 2 == 0 and int(s) < 0:
    t = t + int(s)
  else:
    r = r + int(s)
  s = raw_input()
print str(t) + " " + str(r)
