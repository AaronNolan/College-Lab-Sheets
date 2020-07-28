#!/usr/bin/env python

name = raw_input()
s = raw_input().split(" ")
while s[0] != "end":
  if s[1] == name:
    print " ".join(s)
  s = raw_input().split(" ")
