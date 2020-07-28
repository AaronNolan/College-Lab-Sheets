#!/usr/bin/env python

s = raw_input().split(" ")
while s[0] != "end":
  if int(s[2]) > 7500:
    print " ".join(s)
  s = raw_input().split(" ")
