#!/usr/bin/env python

import sys
l = sys.argv[1:]
i = 0
while i < len(l):
  if int(l[i]) % 2 != 0:
    print l[i]
  i += 1
