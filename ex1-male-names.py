#!/usr/bin/env python

s = raw_input()
while s != "end":
  s = s.split(",")
  a2 = str(s[0]).split()
  if a2[0] == "m":
    a1 = str(s[1]).split()
    a1 = a1[0]
    print str(a1) + " " + str(a2[1])
  s = raw_input()
