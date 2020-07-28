#!/usr/bin/env python

import sys

numbers = {
  "one": "eins",
  "two": "zwei",
  "three": "drei",
  "four": "view",
  "five": "funf",
  "six": "sechs",
  "seven": "sieben",
  "eight": "acht",
  "nine": "neun",
  "ten": "zehn",
}
li = sys.stdin.readlines()

i = 0
while i < len(li):
  s = li[i].strip()
  if s in numbers:
    print numbers[str(s)]
  i += 1
