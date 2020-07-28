#!/usr/bin/env python

import sys
state = sys.argv[1]

header = sys.stdin.readline()
cities = sys.stdin.readlines()

i = 0
while i < len(cities):
   tokens = cities[i].strip().split(",")
   if tokens[9] == state:
      print cities[i].strip()
   i = i + 1
