#!/usr/bin/env python

import sys
l = sys.stdin.readlines()

if len(l) < 11:
  i = 0
  while i < len(l):
    print str(l[i]).rstrip()
    i += 1
else:
  i = 0
  while i < 10:
    print str(l[i]).rstrip()
    i += 1
