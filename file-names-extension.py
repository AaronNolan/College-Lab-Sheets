#!/usr/bin/env python

import sys

s = sys.argv[1]
l = sys.stdin.readlines()

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

t = []
i = 0
while i < len(l):
    li = sep(str(l[i]).rstrip(), "/")
    t.append(li[len(li) - 1])
    i += 1

i = 0
while i < len(t):
    li = sep(str(t[i]).rstrip(), ".")
    if li[len(li) - 1] == str(s):
        print t[i]
    i += 1
