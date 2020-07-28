#!/usr/bin/env python


import sys
with open("Makefile") as f:
  l = f.read()
with open("Makefile.bak", "a") as f:
  f.write(l)
