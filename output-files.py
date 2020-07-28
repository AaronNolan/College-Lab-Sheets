#!/usr/bin/env python

import sys
l = sys.argv[1:]
i = 0
while i < len(l):
  with open(str(l[i])) as f:
      print(f.read().rstrip())
  i += 1
