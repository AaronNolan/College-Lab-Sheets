#!/usr/bin/env python

import sys

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


i = 0
while i < len(l):
    li = sep(str(l[i]).rstrip(), "/")
    print li[len(li) - 1]
    i += 1
