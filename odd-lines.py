#!/usr/bin/env python

import sys
l = sys.stdin.readlines()
i = 0
while i < len(l):
  if int(l[i]) % 2 != 0:
    print str(l[i]).rstrip()
  i += 1
