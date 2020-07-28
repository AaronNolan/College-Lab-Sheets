#!/usr/bin/env python

t = 0
s = raw_input().split("/")
while s[0] != "end":
  if s[len(s) - 1] == "upload":
    t += 1
  s = raw_input().split("/")
print t
