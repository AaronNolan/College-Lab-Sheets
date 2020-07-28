#!/usr/bin/env python

s = raw_input().split()
while s[0] != "end":
  str_1 = s[0].split("-")
  s[0] = " ".join(str_1)
  print " ".join(s)
  s = raw_input().split()
