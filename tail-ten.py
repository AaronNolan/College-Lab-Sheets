#!/usr/bin/env python

import sys
l = sys.stdin.readlines()

if len(l) >= 10:
  i = len(l) - 10
  while i < len(l):
    print str(l[i]).strip()
    i += 1
else:
  i = 0
  while i < len(l):
    print str(l[i]).strip()
    i += 1
