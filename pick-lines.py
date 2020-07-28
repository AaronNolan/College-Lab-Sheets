#!/usr/bin/env python

import sys
s_li = sys.stdin.readlines()
ord_li = sys.argv[1:]
i = 0
while i < len(ord_li):
  a = s_li[int(ord_li[i])].rstrip()
  print a
  i += 1
