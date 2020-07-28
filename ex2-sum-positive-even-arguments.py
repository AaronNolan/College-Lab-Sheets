#!/usr/bin/env python

import sys

li = sys.argv[1:]
t = 0
i = 0
while i < len(li):
  if int(li[i]) > 0:
    if int(li[i]) % 2 == 0:
      t += int(li[i])
  i += 1
print t
