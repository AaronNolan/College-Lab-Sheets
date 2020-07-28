#!/usr/bin/env python

import sys

s = sys.argv[1]
l = sys.stdin.readline().rstrip()

def sep(string, seperator):
    t = []
    i = 0
    p = 0
    while i < len(string):
        if str(string[i]) == str(seperator):
            t.append(string[p:i])
            p = i + 1
        i += 1
    if i == len(string):
        t.append(string[p:i])
    return t

li = sep(l, ",")
print li[int(s)]
